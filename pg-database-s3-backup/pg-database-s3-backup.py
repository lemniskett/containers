#!/usr/bin/env python3

import boto3
import sys
import os
import tempfile
import datetime

S3_URL = os.getenv('S3_URL')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')
S3_PATH_PREFIX = os.getenv('S3_PATH_PREFIX')
DATABASE = sys.argv[1]
LIMIT = int(sys.argv[2])

def main():
    date_string = datetime.datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    with tempfile.TemporaryDirectory() as tmpdir:
        dump_path = os.path.join(tmpdir, 'dump.sql')
        os.system(f'pg_dump -xO {DATABASE} | zstd > {dump_path}.sql.zst')
        s3 = boto3.client(
            's3',
            endpoint_url=S3_URL,
            aws_access_key_id=S3_ACCESS_KEY,
            aws_secret_access_key=S3_SECRET_KEY,
            region_name=S3_REGION
        )
        s3.upload_file(
            f'{dump_path}.sql.zst',
            S3_BUCKET,
            f'{S3_PATH_PREFIX}/{DATABASE}-{date_string}.sql.zst'
        )
        response = s3.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix=f'{S3_PATH_PREFIX}/{DATABASE}-'
        )
        if response['KeyCount'] > LIMIT:
            for obj in response['Contents'][0:response['KeyCount']-LIMIT]:
                s3.delete_object(
                    Bucket=S3_BUCKET,
                    Key=obj['Key']
                )
            
if __name__ == '__main__':
    main()