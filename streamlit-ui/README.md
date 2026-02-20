# Streamlit UI for Auditing Smart FAQ Bot

This is a Streamlit-based web interface that connects directly to the AWS Bedrock Agent.

## Architecture

```
User → Streamlit UI (Lightsail) → AWS Bedrock Agent → Knowledge Base → S3
```

## Files

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies

## Environment Variables Required

The app needs these environment variables set on the Lightsail instance:

```bash
AWS_REGION=us-east-1
AGENT_ID=BAUJICP7L10
AGENT_ALIAS_ID=WTVHMKDT5R
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_SESSION_TOKEN=<your-session-token>  # If using temporary credentials
```

## Local Testing

To test locally before deploying to Lightsail:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables (Windows):
```cmd
set AWS_REGION=us-east-1
set AGENT_ID=BAUJICP7L10
set AGENT_ALIAS_ID=WTVHMKDT5R
set AWS_ACCESS_KEY_ID=your-key
set AWS_SECRET_ACCESS_KEY=your-secret
```

3. Run the app:
```bash
streamlit run app.py
```

4. Open browser to: http://localhost:8501

## Deploying to AWS Lightsail

### Step 1: Create Lightsail Instance

1. Go to AWS Lightsail Console: https://lightsail.aws.amazon.com/
2. Click "Create instance"
3. Select:
   - Platform: Linux/Unix
   - Blueprint: OS Only → Ubuntu 22.04 LTS
   - Instance plan: $3.50/month (512 MB RAM, 1 vCPU)
4. Name it: `auditing-bot-ui`
5. Click "Create instance"

### Step 2: Configure Firewall

1. Click on your instance
2. Go to "Networking" tab
3. Add firewall rule:
   - Application: Custom
   - Protocol: TCP
   - Port: 8501
   - Click "Create"

### Step 3: Connect and Setup

1. Click "Connect using SSH" button
2. Run these commands:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip -y

# Create app directory
mkdir ~/auditing-bot
cd ~/auditing-bot

# Upload files (you'll do this via SFTP or copy-paste)
# For now, create the files manually
```

### Step 4: Upload Files

Use the Lightsail file upload feature or SFTP:
- Upload `app.py`
- Upload `requirements.txt`

### Step 5: Install Dependencies

```bash
cd ~/auditing-bot
pip3 install -r requirements.txt
```

### Step 6: Set Environment Variables

Create a startup script:

```bash
nano ~/auditing-bot/start.sh
```

Add this content:

```bash
#!/bin/bash
export AWS_REGION=us-east-1
export AGENT_ID=BAUJICP7L10
export AGENT_ALIAS_ID=WTVHMKDT5R
export AWS_ACCESS_KEY_ID=your-access-key-here
export AWS_SECRET_ACCESS_KEY=your-secret-key-here
export AWS_SESSION_TOKEN=your-session-token-here

cd ~/auditing-bot
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Make it executable:

```bash
chmod +x ~/auditing-bot/start.sh
```

### Step 7: Run the App

```bash
~/auditing-bot/start.sh
```

### Step 8: Access the UI

Get your Lightsail public IP from the console, then visit:
```
http://YOUR-LIGHTSAIL-IP:8501
```

## Making it Run on Startup (Optional)

Create a systemd service:

```bash
sudo nano /etc/systemd/system/auditing-bot.service
```

Add:

```ini
[Unit]
Description=Auditing Smart FAQ Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/auditing-bot
Environment="AWS_REGION=us-east-1"
Environment="AGENT_ID=BAUJICP7L10"
Environment="AGENT_ALIAS_ID=WTVHMKDT5R"
Environment="AWS_ACCESS_KEY_ID=your-key"
Environment="AWS_SECRET_ACCESS_KEY=your-secret"
ExecStart=/usr/local/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable auditing-bot
sudo systemctl start auditing-bot
sudo systemctl status auditing-bot
```

## Troubleshooting

**App not accessible:**
- Check firewall rules (port 8501 open)
- Verify app is running: `ps aux | grep streamlit`
- Check logs: `journalctl -u auditing-bot -f`

**Agent connection fails:**
- Verify AWS credentials are correct
- Check AGENT_ID and AGENT_ALIAS_ID match your Bedrock agent
- Ensure IAM permissions allow `bedrock:InvokeAgent`

**Dependencies fail to install:**
- Update pip: `pip3 install --upgrade pip`
- Install build tools: `sudo apt install build-essential python3-dev`

## Cost

- Lightsail instance: $3.50/month
- Bedrock API calls: ~$0.01-0.05 per query
- Estimated total: $5-10/month for light usage

## Team

- Team #41
- Sunny Hwang
- Chipo Shereni
