import json
import boto3
import os
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')
bedrock_agent = boto3.client('bedrock-agent')

def handler(event, context):
    """
    Triggered when documents are uploaded to S3.
    Processes PDFs/DOCX and syncs with Bedrock Knowledge Base.
    """
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
        print(f"Processing document: {key}")
        
        try:
            # Extract metadata
            response = s3_client.head_object(Bucket=bucket, Key=key)
            metadata = response.get('Metadata', {})
            
            # Tag document for KB ingestion
            s3_client.put_object_tagging(
                Bucket=bucket,
                Key=key,
                Tagging={
                    'TagSet': [
                        {'Key': 'indexed', 'Value': 'true'},
                        {'Key': 'document_type', 'Value': metadata.get('document_type', 'policy')},
                    ]
                }
            )
            
            print(f"Successfully processed: {key}")
            
            # Note: KB sync happens automatically via S3 data source
            # or can be triggered manually via bedrock-agent API
            
        except Exception as e:
            print(f"Error processing {key}: {str(e)}")
            raise
    
    return {
        'statusCode': 200,
        'body': json.dumps('Documents processed successfully')
    }
