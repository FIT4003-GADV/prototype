"""
Entry-point to the AWS Lambda handler.
"""
from absl import logging

from base_workflow import BaseWorkflow

logging.set_verbosity('debug')
logging.set_stderrthreshold('debug')


def lambda_handler(event, context):
    logging.info(event)
    logging.info(context)
    result = handle(event, context)
    return result


def handle(event, context):
    bw = BaseWorkflow('')
    print(type(event), type(context))
    return 2
