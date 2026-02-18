# Bedrock Setup Guide - Step by Step

## PART 1: Create Knowledge Base (10 minutes)

### Step 1: Go to Bedrock Console
1. Open your browser
2. Go to: https://console.aws.amazon.com/bedrock/
3. Make sure region is set to **US East (N. Virginia)** - check top right corner

### Step 2: Navigate to Knowledge Bases
1. On the left sidebar, click **"Knowledge bases"**
2. Click the orange button **"Create knowledge base"**

### Step 3: Provide Knowledge Base Details
**Page 1 - Knowledge base details:**
- Name: `auditing-kb`
- Description: `Knowledge base for auditing policies and procedures`
- IAM permissions: Select **"Create and use a new service role"**
- Click **"Next"** at the bottom

### Step 4: Set Up Data Source
**Page 2 - Set up data source:**
- Data source name: `auditing-documents`
- S3 URI: Click **"Browse S3"** and select the bucket: `auditing-docs-609350892216`
- Click **"Next"**

### Step 5: Select Embeddings Model
**Page 3 - Select embeddings model:**
- Embeddings model: Select **"Titan Embeddings G1 - Text"** (should be selected by default)
- Click **"Next"**

### Step 6: Configure Vector Store
**Page 4 - Configure vector store:**
- Vector database: Select **"Quick create a new vector store"**
- This will create an OpenSearch Serverless collection automatically
- Click **"Next"**

### Step 7: Review and Create
**Page 5 - Review and create:**
- Review all settings
- Click **"Create knowledge base"**
- Wait 2-3 minutes for creation to complete

### Step 8: Note the Knowledge Base ID
Once created, you'll see a success message.
- Look for **"Knowledge base ID"** - it looks like: `ABCDEFGHIJ`
- **WRITE THIS DOWN** or keep the page open - you'll need it later!

---

## PART 2: Create Bedrock Agent (10 minutes)

### Step 1: Navigate to Agents
1. On the left sidebar, click **"Agents"**
2. Click **"Create Agent"**

### Step 2: Provide Agent Details
**Agent details:**
- Agent name: `auditing-agent`
- Description: `AI assistant for auditing questions`
- User input: Leave **"Enable"** checked
- Click **"Next"**

### Step 3: Select Foundation Model
**Select model:**
- Model: Select **"Anthropic Claude 3 Sonnet"** (or Claude 3.5 Sonnet if available)
- Instructions for the Agent: Copy and paste this:

```
You are an expert auditing assistant. Your role is to help auditors by answering questions about:
- Audit policies and procedures
- Donor rules and regulations
- Standard Operating Procedures (SOPs)
- Internal controls
- Compliance requirements
- Prior audit reports

Always:
1. Provide accurate answers based on the documents in your knowledge base
2. Cite your sources with document names and sections
3. If you don't know something, say so clearly
4. Be concise but thorough
5. Use professional auditing terminology
```

- Click **"Next"**

### Step 4: Add Action Groups (Skip)
**Add action groups:**
- Click **"Next"** (we don't need action groups for now)

### Step 5: Add Knowledge Base
**Add knowledge bases:**
- Click **"Add"**
- Select the knowledge base you created: `auditing-kb`
- Instructions for knowledge base: `Use this knowledge base to answer questions about auditing policies, procedures, and regulations.`
- Click **"Add"**
- Click **"Next"**

### Step 6: Review and Create
**Review and create:**
- Review all settings
- Click **"Create Agent"**
- Wait 1-2 minutes

### Step 7: Prepare the Agent
Once created:
1. Click **"Prepare"** button at the top (this compiles the agent)
2. Wait for "Agent prepared successfully" message

### Step 8: Create an Alias
1. Click **"Create alias"** button
2. Alias name: `prod`
3. Description: `Production version`
4. Click **"Create alias"**

### Step 9: Note the Agent ID and Alias ID
- **Agent ID**: Look for it at the top - looks like: `ABCDEFGHIJ`
- **Alias ID**: After creating alias, you'll see it - looks like: `TSTALIASID` or similar
- **WRITE THESE DOWN** - you'll need them!

---

## PART 3: Test the Agent (2 minutes)

### In the Bedrock Agent Console:
1. Click the **"Test"** button on the right side
2. A chat window will open
3. Try asking: `What is this knowledge base about?`
4. The agent should respond (might say it doesn't have documents yet - that's OK!)

---

## What You Should Have Written Down:
1. ✅ Knowledge Base ID: `__________________`
2. ✅ Agent ID: `__________________`
3. ✅ Agent Alias ID: `__________________`

---

## Next Steps After This:
1. Update Lambda function with Agent ID
2. Upload sample documents to S3
3. Sync the Knowledge Base
4. Test the complete system!

Ready? Let's start with Part 1!
