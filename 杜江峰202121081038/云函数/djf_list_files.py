# -*- coding:utf-8 -*-

import os
import json
from obs import ObsClient


def handler(event, context):
    endPoint = "obs.cn-east-3.myhuaweicloud.com"
    access_key_id='NXQEZPBBGKBUX2NDKMOM'
    secret_access_key='6yCnnML16naxX1sJYkilySEYwrhJaFKTcTfQyN89'
    bucketName = "files-dujiangfeng"
    TestObs = ObsClient(access_key_id=access_key_id, secret_access_key=secret_access_key, server=endPoint)
    listresult = TestObs.listObjects(bucketName)
    objectresults = listresult['body']['contents'][:]
    result = []
    print(event)
    for i in range(0, len(objectresults)):
        result.append({'key': objectresults[i]['key'], 'time': objectresults[i]
                      ['lastModified'], 'size': objectresults[i]['size']})
    jsonArr = json.dumps(result, ensure_ascii=True)
    jsonResponse = {
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers': {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Accept",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE"
        },
        'body': jsonArr,
    }
    return json.dumps(jsonResponse)