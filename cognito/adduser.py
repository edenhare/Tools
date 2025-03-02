import boto3
import os
import datetime
import json
import time
import csv

__POOL_ID__ = "us-east-1_IOEecwytv"
__POOL_ARN__ = "arn:aws:cognito-idp:us-east-1:548985610555:userpool/us-east-1_IOEecwytv"
__DEBUG__ = True
__DEBUG__ = True

def add_one(**kwargs):

    global __POOL_ID__
    global __POOL_ARN__
    
    userData = kwargs['data']
    
    if __DEBUG__ == True:
        print(userData)
        
    client = boto3.client('cognito-idp')

    response = client.admin_create_user(
        UserPoolId=__POOL_ID__,
        Username=userData['email'],
        UserAttributes=[
        {
            'Name': 'phone_number',
            'Value': userData['phone']
        },
        {
            'Name': 'email',
            'Value': userData['email']
        },
        {
            'Name': 'email_verified',
            'Value': 'True'
        },
        {
            'Name': 'phone_number_verified',
            'Value': 'True'
        }
        ],
        ForceAliasCreation=True,
        DesiredDeliveryMediums=[
            'EMAIL',
        ]
    )

    print(response)

    if 'group' in userData:
        response = client.admin_add_user_to_group(
            UserPoolId=__POOL_ID__,
            Username=userData['email'],
            GroupName=userData['group']
    )
    print(response)


    response = client.admin_update_user_attributes(
        UserPoolId=__POOL_ID__,
        Username=userData['email'],
        UserAttributes=[
            {
                'Name': 'birthdate',
                'Value': userData['birthdate'],
            },
            {
                'Name': 'address',
                'Value': userData['address'],
            },
            {
                'Name': 'family_name',
                'Value': userData['family_name'],
            },
            {
                'Name': 'given_name',
                'Value': userData['given_name'],
            },
            {
                'Name': 'middle_name',
                'Value': userData['middle_name'],
            },
            {
                'Name': 'name',
                'Value': userData['name'],
            },
            {
                'Name': 'gender',
                'Value': userData['gender'],
            }
        ]
    )
    print(response)
    return
    
    
def process_bulk(**kwargs):

    userlist = load_csv(csv=kwargs['csv'])
    
    for x in range(0,len(userlist)):
        response = add_one(data=userlist[x])

    return


def load_csv(**kwargs):
    
    userlist = []
    
    csv_file = kwargs['csv']
    
    with open(csv_file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            userData = {}
            userData['email'] = row[0]
            userData['phone'] = row[1]
            try:
                userData['group'] = row[2]
            except Exception as e:
                pass
            userData['birthdate'] = row[3]
            userData['address'] = row[4]
            userData['family_name'] = row[5]
            userData['given_name'] = row[6]
            userData['middle_name'] = row[7]
            userData['name'] = row[6] + " " + row[7] + " " + row[5]
            userData['gender'] = row[8]
            
            userlist.append(userData)

    if __DEBUG__ == True:
        print(f"{len(userlist)} users to add to user pool")
                    
    return(userlist)


def main():
    if __DEBUG__ == True:
        print("adding cognito user to user pool")
        
    process_bulk(csv="users.csv")

    return

if __name__ == "__main__":
    main()
    
