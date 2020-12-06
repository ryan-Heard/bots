import json
import manga.main as messager

def lambda_handler(event, context):
    messager.send_manga()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == '__main__':
    lambda_handler("tests", "tests")