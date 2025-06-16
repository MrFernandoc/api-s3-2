import boto3
import json

def lambda_handler(event, context):
    try:
        bucket_data = event.get('body', {})
        if isinstance(bucket_data, str):
            bucket_data = json.loads(bucket_data)

        bucket_name = bucket_data.get('bucket')

        if not bucket_name:
            return {
                'statusCode': 400,
                'message': 'El campo "bucket" es requerido.'
            }

        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=bucket_name)

        return {
            'statusCode': 200,
            'message': f'Bucket "{bucket_name}" creado exitosamente.'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
