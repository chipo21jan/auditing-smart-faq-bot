# Auditing Smart FAQ Bot

An AI-powered conversational assistant that helps auditors quickly find information from policies, SOPs, donor rules, and audit reports using Amazon Bedrock Knowledge Bases and Agents.

## 🎯 Business Problem

Auditors spend significant time searching through scattered documents (PDFs, SharePoint, emails), leading to:
- Inefficiency and wasted billable hours
- Inconsistent policy interpretations
- Repeated questions to senior staff
- Compliance and quality risks

## 💡 Solution

A conversational AI bot that provides instant, accurate answers with source citations from indexed audit documents.

## 🏗️ Architecture

- **Amazon S3**: Document storage
- **AWS Lambda**: Document processing and agent invocation
- **Amazon Bedrock Knowledge Base**: Document indexing and retrieval
- **Amazon Bedrock Agent**: Natural language Q&A
- **API Gateway**: REST API for web access
- **React Web UI**: User interface

## ✨ Features

- Natural language question answering
- Source citations with document references
- Automatic document indexing
- Scalable and secure
- Real-time responses

## 📋 Prerequisites

- AWS Account with Bedrock access
- Python 3.11+
- Node.js 18+
- AWS CLI configured
- AWS CDK 2.x

## 🚀 Deployment

### 1. Deploy Infrastructure

```bash
cd infrastructure
npm install
cdk bootstrap
cdk deploy
```

### 2. Create Knowledge Base

1. Go to Amazon Bedrock Console
2. Create Knowledge Base with S3 data source
3. Configure OpenSearch Serverless vector store
4. Sync documents

### 3. Create Bedrock Agent

1. Create agent with Claude model
2. Connect Knowledge Base
3. Prepare and create alias

### 4. Upload Documents

```bash
aws s3 cp your-policy.pdf s3://auditing-docs-YOUR-ACCOUNT-ID/
```

Then sync the Knowledge Base in the console.

## 🧪 Testing

### Method 1: Bedrock Console (Recommended for Demo)

1. Sign in to AWS Console
2. Navigate to Amazon Bedrock service
3. Go to **Agents** in the left sidebar
4. Click on your agent (e.g., "auditing-agent")
5. Click the **"Test"** button in the top right
6. Type your question in the chat interface
7. View the answer with source citations

**Example Questions:**
- "What is the procurement threshold for competitive bidding?"
- "What evidence is required for travel expense verification?"
- "Show me segregation of duties requirements for cash handling"

### Method 2: Direct Knowledge Base Testing

1. Go to Amazon Bedrock Console
2. Navigate to **Knowledge Bases**
3. Select your Knowledge Base (e.g., "auditing-kb")
4. Click **"Test"** tab
5. Enter your query and see retrieved documents

### Method 3: API Gateway (For Production)

Once the Lambda function is fully configured:

```bash
curl -X POST https://YOUR-API-GATEWAY-URL/prod/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the procurement threshold for competitive bidding?"}'
```

### Access Requirements

To test the agent, you need:
- AWS Account with Bedrock access
- IAM permissions for Bedrock Agent and Knowledge Base
- Agent must be in "PREPARED" state
- Knowledge Base must be synced with documents

## 📊 Expected Benefits

- **40-60% reduction** in document search time
- **Improved audit quality** through consistent policy application
- **Knowledge retention** when senior staff leave
- **Faster onboarding** for new auditors

## 🔗 AWS Resources

- Knowledge Base ID: `8AOCHBSQQN`
- Agent ID: `BAUJICP7L10`
- S3 Bucket: `auditing-docs-609350892216`
- Region: `us-east-1`

## 📝 Example Questions

- What is the procurement threshold for competitive bidding?
- What evidence is required for travel expense verification?
- Show me segregation of duties requirements for cash handling
- What characterizes an acceptable gift given to an employee?

## 🛠️ Technology Stack

- **Cloud**: AWS (S3, Lambda, Bedrock, API Gateway)
- **AI/ML**: Amazon Bedrock (Claude, Titan Embeddings)
- **Infrastructure**: AWS CDK (TypeScript)
- **Backend**: Python 3.11
- **Frontend**: React, TypeScript

## 📄 License

This project is for hackathon demonstration purposes.

## 👤 Author

chipo21jan

---

Built for AWS Hackathon 2026
