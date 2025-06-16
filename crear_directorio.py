import boto3
import json

def lambda_handler(event, context):
    try:
        data = event.get('body', {})
        if isinstance(data, str):
            data = json.loads(data)

        bucket = data.get('bucket')
        directorio = data.get('directorio')

        if not bucket or not directorio:
            return {
                'statusCode': 400,
                'message': 'Los campos "bucket" y "directorio" son requeridos.'
            }

        if not directorio.endswith('/'):
            directorio += '/'

        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket, Key=directorio)

        return {
            'statusCode': 200,
            'message': f'Directorio "{directorio}" creado en el bucket "{bucket}".'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
