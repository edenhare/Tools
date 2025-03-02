import boto3
import os
import datetime
import json
import time

__POOL_ID__ = "us-east-1_IOEecwytv"
__POOL_ARN__ = "arn:aws:cognito-idp:us-east-1:548985610555:userpool/us-east-1_IOEecwytv"
__DEBUG__ = True

def main():
    global __POOL_ID__
    global __POOL_ARN__
    global __DEBUG__
    
    client = boto3.client('cognito-idp')
    response = client.list_users(
    UserPoolId=__POOL_ID__
    )

    print(response)
    return

if __name__ == "__main__":
    main()
    
