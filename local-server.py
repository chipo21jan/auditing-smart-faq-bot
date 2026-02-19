#!/usr/bin/env python3
"""
Local development server for Auditing Smart FAQ Bot
Runs on localhost:5000 and proxies requests to Bedrock
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

AGENT_ID = 'BAUJICP7L10'
AGENT_ALIAS_ID = 'WTVHMKDT5R'

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.json
        question = data.get('question', '')
        session_id = data.get('session_id', 'default-session')
        
        if not question:
            return jsonify({'error': 'Question is required'}), 400
        
        print(f"Question: {question}")
        print(f"Session: {session_id}")
        
        # Invoke Bedrock Agent
        response = bedrock_agent_runtime.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=question,
            enableTrace=False
        )
        
        # Parse streaming response
        answer = ""
        event_stream = response.get('completion', [])
        
        for event in event_stream:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    chunk_text = chunk['bytes'].decode('utf-8')
                    answer += chunk_text
        
        print(f"Answer: {answer[:100]}...")
        
        if not answer:
            answer = "I received your question but couldn't generate a response. Please try rephrasing."
        
        return jsonify({
            'answer': answer,
            'citations': [],
            'session_id': session_id
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'agent_id': AGENT_ID})

if __name__ == '__main__':
    print("=" * 60)
    print("Auditing Smart FAQ Bot - Local Development Server")
    print("=" * 60)
    print(f"Agent ID: {AGENT_ID}")
    print(f"Agent Alias ID: {AGENT_ALIAS_ID}")
    print(f"Server running on: http://localhost:5000")
    print(f"Chat endpoint: http://localhost:5000/chat")
    print("=" * 60)
    print("\nPress Ctrl+C to stop the server\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
