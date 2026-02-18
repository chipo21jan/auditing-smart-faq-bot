# Architecture Overview

## System Components

### 1. Document Storage (S3)
- Stores all source documents (PDFs, DOCX)
- Versioning enabled for audit trail
- Organized by document type and department
- Triggers Lambda on upload

### 2. Document Processor (Lambda)
- Triggered by S3 events
- Extracts metadata
- Tags documents for indexing
- Monitors processing status

### 3. Bedrock Knowledge Base
- Indexes document content
- Creates vector embeddings
- Chunks documents (300 tokens, 20% overlap)
- Stores in OpenSearch Serverless
- Performs semantic search

### 4. Bedrock Agent
- Orchestrates RAG workflow
- Invokes Knowledge Base for retrieval
- Generates answers using Claude 3
- Returns citations with answers
- Maintains conversation context

### 5. Agent Invoker (Lambda)
- API endpoint for web UI
- Invokes Bedrock Agent
- Parses streaming responses
- Extracts citations
- Manages sessions

### 6. Web UI (React)
- Chat interface
- Displays answers with citations
- Session management
- Example queries

## Data Flow

```
User Question
    ↓
Web UI
    ↓
API Gateway
    ↓
Agent Invoker Lambda
    ↓
Bedrock Agent
    ↓
Knowledge Base (retrieval)
    ↓
Claude 3 (generation)
    ↓
Answer + Citations
    ↓
Web UI
```

## Document Ingestion Flow

```
Document Upload (S3)
    ↓
S3 Event Notification
    ↓
Document Processor Lambda
    ↓
Metadata Extraction & Tagging
    ↓
Knowledge Base Sync
    ↓
Embedding Generation
    ↓
Vector Store (OpenSearch)
```

## RAG Process

1. User asks question
2. Agent receives question
3. Knowledge Base performs semantic search
4. Top K relevant chunks retrieved (default: 5)
5. Claude 3 generates answer using retrieved context
6. Citations extracted from retrieval metadata
7. Answer + citations returned to user

## Security Architecture

- S3: Server-side encryption, bucket policies
- Lambda: IAM roles with least privilege
- Bedrock: Service-linked roles
- API Gateway: Authentication (Cognito/IAM)
- VPC: Optional for enhanced security

## Scalability

- S3: Unlimited storage
- Lambda: Auto-scaling
- Bedrock: Managed service, auto-scaling
- OpenSearch Serverless: Auto-scaling
- API Gateway: Handles high throughput

## Monitoring

- CloudWatch Logs: Lambda execution logs
- CloudWatch Metrics: Invocation counts, errors
- S3 Access Logs: Document access audit
- Bedrock Metrics: Token usage, latency
- X-Ray: Distributed tracing (optional)

## Cost Breakdown

- S3: Storage + requests
- Lambda: Invocations + duration
- Bedrock: Input/output tokens
- OpenSearch Serverless: OCU hours
- Data transfer: Minimal (same region)

Estimated monthly cost for 1000 queries: $50-150
