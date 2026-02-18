import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import { Construct } from 'constructs';

export class AuditingBotStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // S3 bucket for documents
    const documentBucket = new s3.Bucket(this, 'DocumentBucket', {
      bucketName: `auditing-docs-${this.account}`,
      versioned: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: cdk.RemovalPolicy.RETAIN,
    });

    // Lambda for document processing
    const processorFunction = new lambda.Function(this, 'DocumentProcessor', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('../lambda/processor'),
      timeout: cdk.Duration.minutes(5),
      memorySize: 1024,
      environment: {
        BUCKET_NAME: documentBucket.bucketName,
      },
    });

    documentBucket.grantReadWrite(processorFunction);
    
    // Trigger Lambda on S3 upload
    documentBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(processorFunction),
      { suffix: '.pdf' }
    );
    documentBucket.addEventNotification(
      s3.EventType.OBJECT_CREATED,
      new s3n.LambdaDestination(processorFunction),
      { suffix: '.docx' }
    );

    // Bedrock permissions
    processorFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'bedrock:InvokeModel',
        'bedrock:InvokeModelWithResponseStream',
      ],
      resources: ['*'],
    }));

    // Bedrock Agent and Knowledge Base IDs
    const kbId = '8AOCHBSQQN';
    const agentId = 'BAUJICP7L10';
    const agentAliasId = 'WTVHMKDT5R';

    // Lambda for agent invocation
    const agentFunction = new lambda.Function(this, 'AgentInvoker', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('../lambda/agent'),
      timeout: cdk.Duration.seconds(30),
      environment: {
        AGENT_ID: agentId,
        AGENT_ALIAS_ID: agentAliasId,
        KNOWLEDGE_BASE_ID: kbId,
      },
    });

    agentFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'bedrock:InvokeAgent',
        'bedrock:Retrieve',
        'bedrock:RetrieveAndGenerate',
        'bedrock:InvokeModel',
        'bedrock:InvokeModelWithResponseStream',
      ],
      resources: ['*'],
    }));

    // API Gateway for web access
    const api = new apigateway.RestApi(this, 'AuditingBotApi', {
      restApiName: 'Auditing Bot API',
      description: 'API for Auditing Smart FAQ Bot',
      defaultCorsPreflightOptions: {
        allowOrigins: apigateway.Cors.ALL_ORIGINS,
        allowMethods: apigateway.Cors.ALL_METHODS,
        allowHeaders: ['Content-Type', 'Authorization'],
      },
    });

    const agentIntegration = new apigateway.LambdaIntegration(agentFunction);
    const chat = api.root.addResource('chat');
    chat.addMethod('POST', agentIntegration);

    // Outputs
    new cdk.CfnOutput(this, 'DocumentBucketName', {
      value: documentBucket.bucketName,
      description: 'S3 bucket for uploading documents',
    });

    new cdk.CfnOutput(this, 'ProcessorFunctionArn', {
      value: processorFunction.functionArn,
    });

    new cdk.CfnOutput(this, 'AgentFunctionArn', {
      value: agentFunction.functionArn,
    });

    new cdk.CfnOutput(this, 'ApiEndpoint', {
      value: api.url,
      description: 'API Gateway endpoint URL',
    });

    new cdk.CfnOutput(this, 'ChatEndpoint', {
      value: `${api.url}chat`,
      description: 'Chat endpoint for web UI',
    });
  }
}
