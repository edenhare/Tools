import os
import boto3
import configparser


def auth(**kwargs):
    
    print(f"kwargs = {kwargs}")
    try:
        if kwargs['debug'] is not None:
            __DEBUG__ = kwargs['debug']
    except KeyError as e:
            __DEBUG__ = False            
    try:
        if kwargs['credentials'] is not None:
            __CREDENTIALS__ = kwargs['credentials']
    except KeyError as e:
        __CREDENTIALS__ = "credentials.aws"
    try:
        if kwargs['config'] is not None:
            __CONFIGFILE__ = kwargs['config']
    except KeyError as e:
        __CONFIGFILE__ = "config.aws"
    #
    # All requests to AWS have to be authenticated.  
    #
    # the boto3 AWS SDK assumes the credentials have already been configured
    # in the development environment using the CLI and the AWS configure command
    #
    # This script will also look in the curret directory for a file containing
    # the credentials and use them to create the connection.
    #
    if os.path.isfile(__CREDENTIALS__) is True:
        if __DEBUG__ is True:
            print(f"[DEBUG] Local credentials: {__CREDENTIALS__} file exists")
        
        #
        # read app configuration file
        #
        parser = configparser.ConfigParser()
        parser.read(__CREDENTIALS__)
        AWS_ACCESS_KEY = parser.get('default', 'aws_access_key_id')
        AWS_SECRET_KEY = parser.get('default', 'aws_secret_access_key')
    else:
        if __DEBUG__ is True:
            print(f"[DEBUG] No local credentials {__CREDENTIALS__} file.  Assuming CLI credential configuration.")
        AWS_ACCESS_KEY = ""
        AWS_SECRET_KEY = ""

    if os.path.isfile(__CONFIGFILE__) is True:
        if __DEBUG__ is True:
            print(f"[DEBUG] Local configuration {__CONFIGFILE__} file exists")
        
        #
        # read app configuration file
        #
        parser = configparser.ConfigParser()
        parser.read(__CONFIGFILE__)
        AWS_REGION =  parser.get('default', 'region')
        AWS_OUTPUT = parser.get('default','output')
    else:
        if __DEBUG__ is True:
            print(f"[DEBUG] No local configuration {__CONFIGFILE__} file.  Assuming CLI credential configuration.")
        AWS_REGION = ""
        AWS_OUTPUT = ""
        
    return { 'AWS_ACCESS_KEY' : AWS_ACCESS_KEY, 'AWS_SECRET_KEY' : AWS_SECRET_KEY,
        'AWS_REGION' : AWS_REGION, 'AWS_OUTPUT' : AWS_OUTPUT }
    
    
def unit_tests():
    
    print(f"testing function")
    print(f"1 - debug true, default cred files")
    error = False
    result = auth(debug=True)
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")

    print(f"2 - debug false, default cred files")
    error = False    
    result = auth(debug=False)
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
                
    print(f"3 - debug true, name cred, default config")
    error = False    
    result = auth(debug=True,credentials='credentials.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
        
    print(f"4 - debug false, name cred, default config")
    error = False    
    result = auth(debug=False,credentials='credentials.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
        
    print(f"5 - debug true, default cred, name config")
    error = False    
    result = auth(debug=True,config='config.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
        
    print(f"6 - debug false, default cred, name config")
    error = False    
    result = auth(debug=False,config='config.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
        
    print(f"7 - debug true, name cred, name config")
    error = False    
    result = auth(debug=True,credentials='credentials.aws',config='config.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
        
    print(f"8 - debug false, name cred, name config")
    error = False    
    result = auth(debug=False,credentials='credentials.aws',config='config.aws')
    if __DEBUG__ is True:
        print(f"[DEBUG] {result}")
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Access key = {result['AWS_ACCESS_KEY']}")
    else:
        error = True
    if result['AWS_SECRET_KEY'] is not None:
        print(f"Secret key = {result['AWS_SECRET_KEY']}")
    else:
        error = True
    if result['AWS_ACCESS_KEY'] is not None:
        print(f"Region = {result['AWS_REGION']}")
    else:
        error = True
    if result['AWS_OUTPUT'] is not None:
        print(f"Output = {result['AWS_OUTPUT']}")
    else:
        error = True
    if error is True:
        print("[FAIL]")
    else:
        print("[PASS]")
            
if __name__ == "__main__":
    unit_tests()
    
        
    
