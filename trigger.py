import subprocess


def pipelines_trigger(event, context):
    if 'conversion' in event['name']:
        file_name = event['name']
        bucket_name = event['bucket']