"""
Entry-point to the AWS Lambda handler.
"""


def lambda_handler(event, context):
    print(event, context)
    return 'Hello there...'
