# Usage Guide

## Uploading Documents

### Via AWS Console

1. Go to S3 Console
2. Navigate to your DocumentBucket
3. Upload PDFs or DOCX files
4. Add metadata tags (optional):
   - `document_type`: policy, sop, donor_rule, audit_report
   - `department`: finance, hr, it, procurement
   - `effective_date`: YYYY-MM-DD

### Via AWS CLI

```bash
aws s3 cp policy.pdf s3://YOUR_BUCKET/policies/ \
  --metadata document_type=policy,department=finance
```

### Supported Formats

- PDF (recommended)
- DOCX
- TXT
- HTML

## Document Organization

Recommended folder structure:

```
/policies/
  /finance/
  /hr/
  /it/
/donor-rules/
  /usaid/
  /world-bank/
/sops/
/audit-reports/
  /2024/
  /2025/
```

## Asking Questions

### Best Practices

1. Be specific: "What is the travel expense limit for domestic flights?" vs "Tell me about travel"
2. Reference context: "According to USAID rules, what are allowable costs?"
3. Ask for evidence: "What documentation is required for procurement?"
4. Request comparisons: "Compare segregation of duties between cash and inventory"

### Example Queries

#### Policy Interpretation
- "What is the procurement threshold for competitive bidding?"
- "What are the approval levels for capital expenditures?"
- "Explain the conflict of interest policy for board members"

#### Donor Compliance
- "What costs are unallowable under USAID grants?"
- "What are World Bank reporting requirements?"
- "Show me documentation requirements for donor-funded travel"

#### Internal Controls
- "What are segregation of duties requirements for cash handling?"
- "Describe the approval workflow for journal entries"
- "What controls are required for IT system access?"

#### Regulatory Compliance
- "What are the financial reporting deadlines?"
- "Explain data privacy requirements for employee records"

#### Audit Evidence
- "What evidence is needed to verify payroll expenses?"
- "How should fixed asset additions be documented?"

## Understanding Citations

Each answer includes source citations showing:
- Document name and location
- Relevant text excerpt
- Chunk ID for traceability

Use citations to:
- Verify answer accuracy
- Reference original documents
- Build audit documentation

## Session Management

- Each conversation maintains context within a session
- Sessions persist for 1 hour of inactivity
- Start new session for unrelated topics

## Limitations

- Answers based only on indexed documents
- Cannot access external websites or databases
- May not have latest document versions if not synced
- Cannot perform calculations or data analysis

## Troubleshooting

### "No relevant information found"
- Check if documents are uploaded and synced
- Rephrase question with different keywords
- Verify document content is searchable (not scanned images)

### Incorrect or incomplete answers
- Check document quality and formatting
- Ensure KB sync completed successfully
- Try more specific questions

### Slow responses
- Large document sets may take longer
- Check AWS service quotas
- Consider chunking strategy optimization
