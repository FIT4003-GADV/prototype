"""
Entry-point to the AWS Lambda handler.
"""
import json

from absl import logging
import xml.etree.ElementTree as ET

from base_workflow import BaseWorkflow

logging.set_verbosity('info')
logging.set_stderrthreshold('info')

# This property must exist in the input event.
MAIN_EVENT_KEY_NAME = 'svg'


def lambda_handler(event, context):
    logging.debug(f'Received input event: {event}')
    logging.info(f'Context of event: {context}')

    if 'body' not in event:
        raise ValueError('Failed. Missing "body" property in event.')

    decoded_event_body = json.loads(event['body'])

    result = handle(decoded_event_body)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }


def handle(event):
    if MAIN_EVENT_KEY_NAME not in event:
        raise ValueError('Failed. "svg" property must be supplied in event.')
    try:
        try_parse(event['svg'])
        bw = BaseWorkflow(event['svg'])
        return bw.execute()
    except Exception as ex:
        raise ValueError(f'Failed to complete workflow, error: {ex}')


def try_parse(svg_string):
    try:
        ET.fromstring(svg_string)
    except ET.ParseError as err:
        raise ValueError(f'Failed. Input SVG string is not in valid XML format: {err}')
