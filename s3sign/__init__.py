import boto3
import requests
import sys


USAGE_ERROR = 1
EXPIRES_VALUE_ERROR = 2
URL_TEST_ERROR = 3


def generate_pre_signed_url(bucket, key, expires_seconds, http_method):
    url = boto3.client('s3').generate_presigned_url(
        'get_object',
        Params=dict(
            Bucket=bucket,
            Key=key,
        ),
        ExpiresIn=expires_seconds,
        HttpMethod=http_method,
    )
    return url


def parse_args():

    if len(sys.argv) != 4:
        sys.stderr.write('Usage: s3-sign <bucket> <key> <expires>\n')
        sys.exit(USAGE_ERROR)

    bucket = sys.argv[1]
    key = sys.argv[2]
    expires = sys.argv[3]

    time_units = {
        's': 1,
        'm': 60,
        'h': 60 * 60,
        'd': 60 * 60 * 24,
    }

    unit = expires[-1]
    if unit.isdigit():
        unit = 's'
    elif unit in time_units:
        expires = expires[:-1]
    else:
        valid_units = ', '.join(time_units)
        sys.stderr.write('Invalid value for expires\n')
        sys.stderr.write('Valid time units: {}\n'.format(valid_units))
        sys.exit(EXPIRES_VALUE_ERROR)

    if not expires.isdigit():
        sys.stderr.write('Invalid value for expires\n')
        sys.stderr.write('Example expires values: 30s, 5m, 2h, 3d\n')
        sys.exit(EXPIRES_VALUE_ERROR)

    return (
        bucket,
        key,
        int(expires) * time_units[unit],
    )


def test_url(url):
    try:
        response = requests.head(url, stream=True)
        if response.status_code != 200:
            raise Exception(response.status_code)
    except Exception as error:
        sys.stderr.write('HEAD {}\n'.format(url))
        sys.stderr.write('Error: {}\n'.format(error))
        sys.exit(URL_TEST_ERROR)
