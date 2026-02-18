# What We'll Do After Node.js Installs

## Step 1: Verify Node.js Installation (2 minutes)
- Close current command prompt
- Open NEW command prompt
- Check: `node --version` → should show v24.13.1
- Check: `npm --version` → should show 10.x.x

## Step 2: Install AWS CDK (3 minutes)
This is the tool that will deploy your infrastructure to AWS.

Command:
```cmd
npm install -g aws-cdk
```

Then verify:
```cmd
cdk --version
```

## Step 3: Check Bedrock Access (1 minute)
Make sure your AWS account can use Amazon Bedrock (the AI service).

Command:
```cmd
aws bedrock list-foundation-models --region us-east-1
```

Expected: Long list of AI models
If error: We'll request Bedrock access in AWS Console

## Step 4: Set Your AWS Region (1 minute)
Make sure you're using a region that supports Bedrock.

Check current region:
```cmd
aws configure get region
```

Set to us-east-1 if needed:
```cmd
aws configure set region us-east-1
```

## Step 5: Bootstrap AWS CDK (2 minutes)
This prepares your AWS account to use CDK (only needed once per account).

Command:
```cmd
cdk bootstrap
```

This creates an S3 bucket and other resources CDK needs.

---

## Total Time Estimate
About 10-15 minutes to complete all verification steps.

After this, we'll be ready to:
1. Deploy the infrastructure
2. Set up Bedrock Knowledge Base
3. Upload documents
4. Test the bot!

---

Don't worry - I'll guide you through each step one at a time!
