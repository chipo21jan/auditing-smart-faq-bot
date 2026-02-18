import json
import boto3
import os
import uuid

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

def handler(event, context):
    """
    Invokes Bedrock Agent to answer auditor questions.
    Returns answer with source citations.
    """
    
    agent_id = os.environ.get('AGENT_ID', 'BAUJICP7L10')
    agent_alias_id = os.environ.get('AGENT_ALIAS_ID', 'WTVHMKDT5R')
    
    # Handle OPTIONS request for CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': ''
        }
    
    # Extract question from request
    try:
        body = json.loads(event.get('body', '{}'))
        question = body.get('question', '')
        session_id = body.get('session_id', str(uuid.uuid4()))
    except:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({'error': 'Invalid request body'})
        }
    
    if not question:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({'error': 'Question is required'})
        }
    
    try:
        print(f"Invoking agent {agent_id} with alias {agent_alias_id}")
        print(f"Question: {question}")
        print(f"Session: {session_id}")
        
        # Try using just the first 10 characters of agent ID
        short_agent_id = agent_id[:10] if len(agent_id) > 10 else agent_id
        print(f"Using shortened agent ID: {short_agent_id}")
        
        # Invoke agent using invoke_agent API
        response = bedrock_agent_runtime.invoke_agent(
            agentId=short_agent_id,
            agentAliasId=agent_alias_id,
            sessionId=session_id,
            inputText=question,
            enableTrace=False
        )
        
        print("Got response from agent, processing stream...")
        
        # Parse streaming response
        answer = ""
        event_stream = response.get('completion', [])
        
        for event in event_stream:
            if 'chunk' in event:
                chunk = event['chunk']
                if 'bytes' in chunk:
                    chunk_text = chunk['bytes'].decode('utf-8')
                    answer += chunk_text
                    print(f"Chunk: {chunk_text}")
        
        print(f"Final answer length: {len(answer)}")
        
        if not answer:
            answer = "I received your question but couldn't generate a response. Please try rephrasing your question."
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({
                'answer': answer,
                'citations': [],
                'session_id': session_id
            })
        }
        
    except Exception as e:
        error_msg = str(e)
        print(f"Error invoking agent: {error_msg}")
        import traceback
        traceback.print_exc()
        
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST,OPTIONS'
            },
            'body': json.dumps({
                'error': f'Agent invocation failed: {error_msg}',
                'details': 'Check CloudWatch logs for more information'
            })
        }
