# Hackathon Demo Script - Auditing Smart FAQ Bot

**Team #41**: Chipo Shereni & Sunny Hwang  
**Time**: 5 minutes  
**Live Demo URL**: http://54.90.193.128:8501/

---

## 🎬 Opening (30 seconds)

"Hi, I'm [Your Name] from Team 41. We built an AI-powered Auditing Smart FAQ Bot that transforms how auditors access information.

Instead of spending hours searching through scattered PDFs and policies, auditors can now ask natural language questions and get instant, accurate answers with source citations."

---

## 📊 The Problem (30 seconds)

"Auditors currently face three major challenges:

1. **Time waste** - Hours spent manually searching documents
2. **Inconsistency** - Different interpretations of the same policies
3. **Knowledge gaps** - Dependency on senior staff for answers

This costs organizations thousands in billable hours and creates compliance risks."

---

## 💡 Our Solution (30 seconds)

"We built a conversational AI assistant using AWS Bedrock that:
- Understands natural language questions
- Searches through indexed audit documents
- Returns accurate answers with source citations
- Works 24/7 with no waiting"

---

## 🎯 Live Demo (2 minutes)

### Setup
1. **Open browser** to http://54.90.193.128:8501/
2. **Show the interface** - clean, simple chat UI

### Demo Question 1: Procurement Policy
**Type:** "What is the procurement threshold for competitive bidding?"

**While waiting for response, say:**
"The bot is querying our Knowledge Base, which contains audit policies, SOPs, and compliance documents stored in S3 and indexed using Amazon Bedrock."

**When answer appears:**
"Notice it gives us the exact threshold - $25,000 - and provides source citations showing which document and section this came from. This is critical for audit trail compliance."

### Demo Question 2: Travel Expenses
**Type:** "What evidence is required for travel expense verification?"

**Say:**
"Let's try a different topic - travel expenses. This shows the bot can handle various audit domains."

**When answer appears:**
"Again, we get a detailed answer with specific requirements and source citations. An auditor can immediately verify this information."

### Demo Question 3 (If Time Permits): Segregation of Duties
**Type:** "Show me segregation of duties requirements for cash handling"

**Say:**
"One more - a complex control question about segregation of duties."

**When answer appears:**
"The bot understands the context and retrieves relevant control requirements."

---

## 🏗️ Architecture (45 seconds)

**Show GitHub repository** (optional - if you have it open in another tab)

"Here's how it works technically:

**Backend:**
- Documents stored in **S3**
- **Lambda** processes uploads automatically
- **Bedrock Knowledge Base** indexes documents using Titan embeddings
- **OpenSearch Serverless** provides vector search
- **Bedrock Agent** with Claude 3.5 Sonnet answers questions

**Frontend:**
- **Streamlit UI** deployed on **Lightsail**
- Clean, responsive interface
- Real-time streaming responses

Everything is infrastructure-as-code using **AWS CDK**, making it reproducible and scalable."

---

## 💰 Business Impact (30 seconds)

"The expected benefits are significant:

- **40-60% reduction** in document search time
- **Improved audit quality** through consistent policy application
- **Knowledge retention** - institutional knowledge stays even when people leave
- **Faster onboarding** - new auditors productive from day one

For a team of 10 auditors, this could save **$100,000+ annually** in billable hours."

---

## 🚀 Technical Highlights (30 seconds)

"What makes this impressive technically:

1. **RAG Architecture** - Retrieval-Augmented Generation ensures answers are grounded in real documents
2. **Serverless & Scalable** - Handles 1 user or 1,000 users automatically
3. **Production-ready** - Complete with error handling, citations, and audit trails
4. **Secure** - All data stays in your AWS account with IAM controls
5. **Cost-effective** - ~$5-10/month for light usage"

---

## 🎯 Closing (15 seconds)

"This Auditing Smart FAQ Bot demonstrates how AI can augment professional knowledge workers. We've built a production-ready solution that solves real business problems using AWS's latest AI capabilities.

Thank you! Happy to answer questions."

---

## 🆘 Backup Plans

### If Demo Site is Down:
"We have a backup - let me show you the Bedrock Console test interface where the agent is running."
- Navigate to Bedrock Console
- Show agent test interface
- Run the same questions

### If Questions Don't Work Well:
"The bot works best with questions about the policies we've uploaded. Let me show you the architecture and code instead."
- Show GitHub repository
- Walk through the CDK infrastructure code
- Explain the Bedrock Agent configuration

### If Internet is Slow:
"While that's loading, let me explain the architecture..."
- Talk through the diagram
- Explain the technical implementation
- Show the code on GitHub

---

## 📝 Anticipated Questions & Answers

**Q: How accurate is it?**  
A: "The AI only answers based on uploaded documents using RAG, so accuracy matches your source documents. Plus, it includes citations so auditors can verify."

**Q: What about data security?**  
A: "All data stays in your AWS account. Documents are encrypted at rest and in transit. IAM controls who can access what. No data goes to third parties."

**Q: How much does it cost?**  
A: "Bedrock charges per API call - about $0.01-0.05 per query. For a team of 10 auditors, estimated cost is $50-100/month. Compare that to billable hours saved!"

**Q: Can it replace auditors?**  
A: "No, it's an assistant tool. Auditors still need to interpret, analyze, and make judgments. This just makes them more efficient at finding information."

**Q: How long to deploy?**  
A: "With our code on GitHub, infrastructure deployment takes about 30 minutes using CDK. Adding documents and syncing takes another 10-15 minutes per batch."

**Q: What if the document isn't in the Knowledge Base?**  
A: "The agent will say it doesn't have that information. This is better than hallucinating an answer. You can then upload the missing document."

---

## ✅ Pre-Demo Checklist

- [ ] Test the live URL works: http://54.90.193.128:8501/
- [ ] Have GitHub repo open in a tab: https://github.com/chipo21jan/auditing-smart-faq-bot
- [ ] Have Bedrock Console open as backup
- [ ] Test all 3 demo questions beforehand
- [ ] Close unnecessary browser tabs
- [ ] Set browser zoom to 125% for visibility
- [ ] Have water nearby
- [ ] Take a deep breath!

---

## 🎤 Presentation Tips

1. **Speak clearly and confidently** - You built something real!
2. **Make eye contact** with judges
3. **Show enthusiasm** about the technology
4. **Let responses fully load** before commenting
5. **Point out the citations** - this is a key differentiator
6. **Emphasize business value** not just tech features
7. **Be ready to pivot** if something doesn't work
8. **Smile!** You've accomplished a lot

---

## 🏆 Why You'll Win

1. ✅ **Solves a real problem** - Not a toy demo
2. ✅ **Production-ready** - Complete, documented, deployable
3. ✅ **Uses latest AWS tech** - Bedrock, Claude 3.5, RAG
4. ✅ **Clear business value** - ROI with time/cost savings
5. ✅ **Live demo** - Actually works, not just slides
6. ✅ **Team collaboration** - Shows teamwork
7. ✅ **Open source ready** - Code on GitHub, well documented

---

**Good luck! You've got this! 🚀**
