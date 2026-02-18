# Testing Guide - Auditing Smart FAQ Bot

This guide explains how to test the Auditing Smart FAQ Bot after deployment.

## Prerequisites

Before testing, ensure:
- ✅ AWS infrastructure is deployed (CDK stack)
- ✅ Bedrock Knowledge Base is created and synced
- ✅ Bedrock Agent is created and prepared
- ✅ At least one document is uploaded to S3 and indexed
- ✅ You have AWS Console access with Bedrock permissions

## Testing Methods

### 🎯 Method 1: Bedrock Agent Console (RECOMMENDED)

This is the easiest and most reliable way to test your agent.

**Steps:**

1. **Sign in to AWS Console**
   - Go to https://console.aws.amazon.com
   - Sign in with your credentials

2. **Navigate to Bedrock**
   - Search for "Bedrock" in the services search bar
   - Click on "Amazon Bedrock"

3. **Open Your Agent**
   - Click "Agents" in the left sidebar
   - Find and click your agent (e.g., "auditing-agent")
   - Agent status should show "PREPARED"

4. **Start Testing**
   - Click the **"Test"** button in the top right corner
   - A chat interface will appear on the right side

5. **Ask Questions**
   - Type your question in the input box
   - Press Enter or click Send
   - Wait for the response (usually 3-10 seconds)

6. **Review Results**
   - Read the answer
   - Check the source citations
   - Verify the information is accurate

**Example Test Questions:**

```
What is the procurement threshold for competitive bidding?

What evidence is required for travel expense verification?

Show me segregation of duties requirements for cash handling.

What characterizes an acceptable gift given to an employee?

What are the password complexity requirements?
```

**Expected Response Format:**
```
Answer: [Detailed answer based on your documents]

Sources:
- s3://auditing-docs-ACCOUNT-ID/sample-audit-policy.txt
- Confidence score: 0.85
```

---

### 🔍 Method 2: Knowledge Base Testing

Test the Knowledge Base retrieval directly (without the agent).

**Steps:**

1. Go to Amazon Bedrock Console
2. Click **"Knowledge Bases"** in the left sidebar
3. Select your Knowledge Base (e.g., "auditing-kb")
4. Click the **"Test"** tab
5. Enter a query in the search box
6. View the retrieved document chunks

**What This Tests:**
- Document indexing is working
- Vector search is finding relevant content
- Embeddings are properly created

**Example Query:**
```
procurement threshold competitive bidding
```

**Expected Result:**
- Shows relevant text chunks from your documents
- Displays similarity scores
- Shows source document references

---

### 🌐 Method 3: API Gateway (Advanced)

Test via the REST API endpoint (requires API Gateway to be working).

**Using PowerShell:**

```powershell
Invoke-RestMethod -Uri 'https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/prod/chat' `
  -Method Post `
  -ContentType 'application/json' `
  -Body '{"question":"What is the procurement threshold for competitive bidding?"}'
```

**Using curl (if installed):**

```bash
curl -X POST https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/prod/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the procurement threshold for competitive bidding?"}'
```

**Expected Response:**

```json
{
  "answer": "According to the procurement policy, the competitive bidding thresholds are...",
  "citations": [
    {
      "text": "Purchases over $25,000 require...",
      "source": "s3://auditing-docs-609350892216/sample-audit-policy.txt",
      "score": 0.85
    }
  ],
  "session_id": "session-1234567890"
}
```

---

## Troubleshooting

### Agent Not Responding

**Problem:** Agent test interface shows no response or error

**Solutions:**
1. Check agent status is "PREPARED" (not "DRAFT")
2. Verify Knowledge Base is connected to the agent
3. Ensure at least one document is synced in the Knowledge Base
4. Check IAM permissions for Bedrock Agent

### No Documents Found

**Problem:** Agent says "I don't have information about that"

**Solutions:**
1. Verify documents are uploaded to S3 bucket
2. Check Knowledge Base sync status (must show "Available")
3. Re-sync the Knowledge Base data source
4. Ensure documents are in supported formats (PDF, TXT, DOCX)

### API Gateway 500 Error

**Problem:** API returns Internal Server Error

**Solutions:**
1. Check Lambda function logs in CloudWatch
2. Verify Lambda has correct environment variables
3. Ensure Lambda IAM role has Bedrock permissions
4. Check Lambda function is not timing out

---

## Test Scenarios for Demo

### Scenario 1: Procurement Policy
**Question:** "What is the procurement threshold for competitive bidding?"

**Expected Answer:** Should mention $25,000 threshold and quote requirements

### Scenario 2: Travel Expenses
**Question:** "What evidence is required for travel expense verification?"

**Expected Answer:** Should list required documentation (receipts, approvals, etc.)

### Scenario 3: Internal Controls
**Question:** "Show me segregation of duties requirements for cash handling"

**Expected Answer:** Should explain separation of responsibilities

### Scenario 4: HR Policy
**Question:** "What characterizes an acceptable gift given to an employee?"

**Expected Answer:** Should mention gift value limits and disclosure requirements

### Scenario 5: IT Security
**Question:** "What are the password complexity requirements?"

**Expected Answer:** Should list password rules (length, characters, expiration)

---

## Performance Metrics

**Response Time:**
- Typical: 3-10 seconds
- Depends on: document size, query complexity, model selection

**Accuracy:**
- Should cite correct source documents
- Answers should be grounded in uploaded content
- Citations should include document names and locations

---

## Access Information

**AWS Resources:**
- Account: 609350892216
- Region: us-east-1
- Knowledge Base ID: 8AOCHBSQQN
- Agent ID: BAUJICP7L10
- Agent Alias: AuditAgent007
- S3 Bucket: auditing-docs-609350892216

**Console Links:**
- Agent: https://console.aws.amazon.com/bedrock/home?region=us-east-1#/agents/BAUJICP7L10
- Knowledge Base: https://console.aws.amazon.com/bedrock/home?region=us-east-1#/knowledge-bases/8AOCHBSQQN
- S3 Bucket: https://s3.console.aws.amazon.com/s3/buckets/auditing-docs-609350892216

---

## For Hackathon Judges

To test this project:

1. **Request AWS Console Access** (read-only Bedrock permissions)
2. **Navigate to the Agent** using the link above
3. **Click "Test"** button
4. **Ask any of the example questions** provided
5. **Observe:**
   - Natural language understanding
   - Accurate answers from documents
   - Source citations
   - Response time

**No setup required** - the agent is already deployed and ready to test!

---

## Next Steps

After successful testing:
- Upload more policy documents to S3
- Sync Knowledge Base to index new documents
- Test with domain-specific questions
- Gather user feedback
- Monitor usage in CloudWatch
