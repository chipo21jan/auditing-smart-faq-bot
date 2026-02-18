# Deployment Guide

## Prerequisites

- AWS Account with Bedrock access enabled
- AWS CLI configured
- Node.js 18+ and npm
- Python 3.11+

## Step 1: Deploy Infrastructure

```bash
cd infrastructure
npm install
cdk bootstrap  # First time only
cdk deploy
```

Note the outputs: DocumentBucketName, AgentFunctionArn

## Step 2: Create Bedrock Knowledge Base (AWS Console)

1. Go to Amazon Bedrock Console → Knowledge Bases
2. Click "Create knowledge base"
3. Configure:
   - Name: `auditing-kb`
   - IAM role: Create new or use existing
   - Embedding model: `amazon.titan-embed-text-v1`
4. Add S3 data source:
   - Select the DocumentBucket from CDK output
   - Chunking: Default (300 tokens, 20% overlap)
5. Create vector store (OpenSearch Serverless recommended)
6. Note the Knowledge Base ID

## Step 3: Create Bedrock Agent (AWS Console)

1. Go to Amazon Bedrock Console → Agents
2. Click "Create agent"
3. Configure:
   - Name: `auditing-agent`
   - Model: `anthropic.claude-3-sonnet-20240229-v1:0`
   - Instructions: "You are an auditing assistant. Answer questions about policies, SOPs, donor rules, and audit reports. Always cite your sources."
4. Add Knowledge Base:
   - Select the KB created in Step 2
   - Instructions: "Use this to answer questions about auditing policies and procedures"
5. Create alias: `prod`
6. Note the Agent ID and Alias ID

## Step 4: Update Lambda Configuration

Update the CDK stack parameters:

```bash
cdk deploy --parameters KnowledgeBaseId=YOUR_KB_ID --parameters AgentId=YOUR_AGENT_ID
```

## Step 5: Upload Sample Documents

```bash
aws s3 cp docs/sample-policy.pdf s3://YOUR_BUCKET_NAME/policies/
aws s3 cp docs/donor-rules.pdf s3://YOUR_BUCKET_NAME/donor-rules/
```

## Step 6: Sync Knowledge Base

In Bedrock Console → Knowledge Bases → Data Sources → Click "Sync"

## Step 7: Deploy Web UI

1. Create API Gateway for the AgentInvoker Lambda
2. Update `web/src/App.tsx` with the API endpoint
3. Deploy:

```bash
cd web
npm install
npm start  # Development
npm run build  # Production
```

## Testing

Test the agent directly:

```bash
aws bedrock-agent-runtime invoke-agent \
  --agent-id YOUR_AGENT_ID \
  --agent-alias-id YOUR_ALIAS_ID \
  --session-id test-session \
  --input-text "What is the procurement threshold?" \
  output.txt
```

## Cost Optimization

- Use S3 Intelligent-Tiering for document storage
- Set Lambda reserved concurrency limits
- Use OpenSearch Serverless for variable workloads
- Monitor Bedrock token usage

## Security

- Enable S3 bucket encryption
- Use VPC endpoints for Bedrock
- Implement IAM least privilege
- Enable CloudTrail logging
- Add API Gateway authentication (Cognito/IAM)
