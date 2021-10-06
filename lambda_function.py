"""
Entry-point to the AWS Lambda handler.
"""
from absl import logging

from base_workflow import BaseWorkflow

logging.set_verbosity('debug')
logging.set_stderrthreshold('debug')

# This property must exist in the input event.
MAIN_EVENT_KEY_NAME = 'svg'


def lambda_handler(event, context):
    logging.debug(f'Received input event: {event}, with context: {context}')
    result = handle(event)
    return result


def handle(event):
    if MAIN_EVENT_KEY_NAME not in event:
        raise ValueError('Failed. "svg" property must be supplied in event.')
    try:
        bw = BaseWorkflow(event['svg'])
        return bw.execute()
    except Exception as ex:
        raise ValueError(f'Failed to complete workflow, error: {ex}')
