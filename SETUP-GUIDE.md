# Step-by-Step Setup Guide for Beginners

## What We're Going to Do

Think of this like building a smart assistant that reads your audit documents and answers questions about them. We need to:
1. Check your computer has the right tools installed
2. Set up AWS (Amazon's cloud) to store documents and run the assistant
3. Create a website where auditors can ask questions

Let's verify everything step by step.

---

## STEP 1: Check Your Python Installation

### What is Python?
Python is a programming language. We need it to run some of the code that processes documents.

### Let's Check:

Open your command prompt (CMD) or PowerShell and type:

```cmd
python --version
```

**What you should see:** Something like `Python 3.11.x` or `Python 3.10.x`

**✅ Good:** Version 3.10 or higher
**❌ Problem:** Version below 3.10 or "command not found"

If you have a problem, we'll fix it together.

---

## STEP 2: Check Your AWS CLI Installation

### What is AWS CLI?
AWS CLI is a tool that lets you control Amazon's cloud services from your computer (instead of clicking around in a website).

### Let's Check:

In your command prompt, type:

```cmd
aws --version
```

**What you should see:** Something like `aws-cli/2.x.x Python/3.x.x Windows/...`

**✅ Good:** Version 2.x
**❌ Problem:** Version 1.x or "command not found"

### Check if AWS CLI is Connected to Your Account:

Type:

```cmd
aws sts get-caller-identity
```

**What you should see:** Your AWS account number and user information in JSON format

**❌ If you see an error:** Your AWS CLI is not configured correctly

---

## STEP 3: Check Your AWS Account Permissions

### What We Need to Check:
Your AWS account needs permission to use certain services. Since you have a non-root account, we need to verify you have the right permissions.

### Let's Check Bedrock Access:

In command prompt, type:

```cmd
aws bedrock list-foundation-models --region us-east-1
```

**✅ Good:** You see a long list of AI models
**❌ Problem:** Error message about permissions or "Bedrock is not available"

**Important:** If Bedrock is not available, you may need to:
1. Request access in the AWS Console (I'll show you how)
2. Ask your AWS administrator to enable Bedrock for your account

---

## STEP 4: Install Node.js (Required for the Infrastructure Code)

### What is Node.js?
Node.js lets us run JavaScript code on your computer. We need it to deploy the AWS infrastructure.

### Let's Check if You Have It:

In command prompt, type:

```cmd
node --version
```

**✅ Good:** Version 18.x or higher
**❌ Problem:** "command not found" or version below 18

### If You Need to Install Node.js:

1. Go to: https://nodejs.org/
2. Download the "LTS" version (Long Term Support)
3. Run the installer
4. Keep clicking "Next" with default settings
5. Restart your command prompt
6. Check again with `node --version`

---

## STEP 5: Install AWS CDK (The Tool to Deploy Infrastructure)

### What is AWS CDK?
CDK (Cloud Development Kit) is a tool that helps us create AWS resources (like storage buckets, functions) using code instead of clicking around.

### Install CDK:

In command prompt, type:

```cmd
npm install -g aws-cdk
```

Wait for it to finish (might take 2-3 minutes).

### Check if it Worked:

```cmd
cdk --version
```

**✅ Good:** You see a version number like `2.x.x`

---

## STEP 6: Check Your AWS Region

### What is a Region?
AWS has data centers around the world. We need to pick one close to you for faster performance.

### Check Your Current Region:

```cmd
aws configure get region
```

**Recommended regions for Bedrock:**
- `us-east-1` (Virginia, USA)
- `us-west-2` (Oregon, USA)
- `eu-west-1` (Ireland, Europe)

### If You Need to Change Region:

```cmd
aws configure set region us-east-1
```

---

## Summary Checklist

Before we continue, make sure you have:

- [ ] Python 3.10+ installed
- [ ] AWS CLI 2.x installed and configured
- [ ] AWS CLI can connect to your account (`aws sts get-caller-identity` works)
- [ ] Bedrock access enabled (or requested)
- [ ] Node.js 18+ installed
- [ ] AWS CDK installed
- [ ] AWS region set to a Bedrock-supported region

---

## What to Do Next

Once you've completed this checklist, tell me:
1. Which checks passed ✅
2. Which checks failed ❌
3. Any error messages you saw

I'll help you fix any problems before we move to the next step!
