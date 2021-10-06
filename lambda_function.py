"""
Entry-point to the AWS Lambda handler.
"""
from absl import logging


def lambda_handler(event, context):
    logging.info(event)
    logging.info(context)
    result = handle(event, context)
    return result


def handle(event, context):
    print(type(event), type(context))
    return 2
