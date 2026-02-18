import json
import boto3
import os
import uuid

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')

def handler(event, context):
    """
    Uses Bedrock Knowledge Base to answer auditor questions.
    Returns answer with source citations.
    """
    
    knowledge_base_id = os.environ['KNOWLEDGE_BASE_ID']
    
    # Extract question from request
    body = json.loads(event.get('body', '{}'))
    question = body.get('question', '')
    session_id = body.get('session_id', str(uuid.uuid4()))
    
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
        print(f"Using Knowledge Base: {knowledge_base_id}")
        print(f"Question: {question}")
        
        # Use retrieve and generate API with default model
        response = bedrock_agent_runtime.retrieve_and_generate(
            input={
                'text': question
            },
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': knowledge_base_id,
                    'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1'
                }
            }
        )
        
        print(f"Got response from Knowledge Base")
        
        # Extract answer and citations
        answer = response.get('output', {}).get('text', 'No answer generated')
        
        citations = []
        for citation in response.get('citations', []):
            for ref in citation.get('retrievedReferences', []):
                citations.append({
                    'text': ref.get('content', {}).get('text', ''),
                    'source': ref.get('location', {}).get('s3Location', {}).get('uri', 'Unknown'),
                    'score': ref.get('metadata', {}).get('score', 0)
                })
        
        print(f"Final answer: {answer}")
        print(f"Citations count: {len(citations)}")
        
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
                'citations': citations,
                'session_id': session_id
            })
        }
        
    except Exception as e:
        print(f"Error invoking agent: {str(e)}")
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
            'body': json.dumps({'error': str(e)})
        }
