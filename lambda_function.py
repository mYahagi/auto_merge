import requests
import json
import os
import re
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    apiKey = os.environ['yuor_access_token']
    urlKeys = [
        'hoge1_repo_url',
        'hoge2_repo_url',
        'hoge3_repo_url',
        'hoge4_repo_url'
        ]

    baseRepo = 'develop'
    headRepo = 'share'
    commitMessage = '日時マージ'
    
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': 'token {}'.format(apiKey)
    }
    
    data = {
        'base': baseRepo,
        'head': headRepo,
        'commit_message': commitMessage
    }

    try:
        for key in urlKeys:
            response = requests.post(os.environ[key], headers=headers, data=json.dumps(data))
            logger.info(response.text)
    except Exception as e:
        logger.error(e)
