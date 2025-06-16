import boto3
import json
import base64

def lambda_handler(event, context):
    try:
        data = event.get('body', {})
        if isinstance(data, str):
            data = json.loads(data)

        bucket = data.get('bucket')
        directorio = data.get('directorio', '')
        nombre_archivo = data.get('archivo')
        contenido_base64 = data.get('contenido')

        if not all([bucket, nombre_archivo, contenido_base64]):
            return {
                'statusCode': 400,
                'message': 'Los campos "bucket", "archivo" y "contenido" son requeridos.'
            }

        if directorio and not directorio.endswith('/'):
            directorio += '/'

        ruta_objeto = directorio + nombre_archivo
        contenido_binario = base64.b64decode(contenido_base64)

        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket, Key=ruta_objeto, Body=contenido_binario)

        return {
            'statusCode': 200,
            'message': f'Archivo "{ruta_objeto}" subido correctamente al bucket "{bucket}".'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
