# s3-sign
Generates pre-signed URLs for S3.

At this time, only GET requests are supported.

# Installation

    pip install s3-sign

# Configuration

S3 uses Boto 3, which requires configuration.

See https://boto3.readthedocs.org/

In short, set up your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
environment variables.

# Usage

    s3-sign <bucket> <key> <expires>

Example expires values:
- 30s = 30 seconds
- 10m = 10 minutes
- 5h = 5 hours
- 2d = 2 days
