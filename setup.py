#!/usr/bin/env python

from setuptools import setup

setup(
    name='s3-sign',
    version='0.2',
    description='Generates pre-signed URLs for S3.',
    author='Raymond Butcher',
    author_email='ray@bashton.com',
    url='https://github.com/BashtonLtd/s3-sign',
    license='Apache License 2.0',
    packages=(
        's3sign',
    ),
    scripts=(
        'bin/s3-sign',
    ),
    install_requires=(
        'boto3',
        'requests',
    ),
)
