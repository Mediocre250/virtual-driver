import os
import json
from obs import ObsClient


def handler(event, context):
    endPoint = "obs.cn-east-3.myhuaweicloud.com"
    access_key_id='NXQEZPBBGKBUX2NDKMOM'
    secret_access_key='6yCnnML16naxX1sJYkilySEYwrhJaFKTcTfQyN89'
    bucketName = "files-dujiangfeng"
    formParams = {}
    formParams['x-obs-acl'] = 'public-read'
    formParams['content-type'] = 'text/plain'
    TestObs = ObsClient(access_key_id=access_key_id, secret_access_key=secret_access_key, server=endPoint)
    resp = TestObs.createPostSignature(expires=3600, formParams=formParams)
    mapx = {}
    mapx["policy"] = resp['policy']
    mapx["access_key_id"] = access_key_id
    mapx["signature"] = resp["signature"]
    jsonResponse = {
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers': {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Accept",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE"
        },
        'body': json.dumps(mapx)
    }
    return json.dumps(jsonResponse)
