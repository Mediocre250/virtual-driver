import os
import json
from obs import ObsClient
import base64

def handler(event, context):
    endPoint = "obs.cn-east-3.myhuaweicloud.com"
    access_key_id='NXQEZPBBGKBUX2NDKMOM'
    secret_access_key='6yCnnML16naxX1sJYkilySEYwrhJaFKTcTfQyN89'
    bucketName = "files-dujiangfeng"
    TestObs = ObsClient(access_key_id=access_key_id, secret_access_key=secret_access_key, server=endPoint)
    file_name = str(base64.b64decode(event['body']))
    #file_name = file_name[8:-5]
    file_name = file_name[11:-1]
    print(file_name)
    res = TestObs.createSignedUrl('GET', bucketName, file_name, expires=3600)
    jsonResponse = {
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers': {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Accept",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE"
        },
        'body': res.signedUrl,
    }
    return json.dumps(jsonResponse)
