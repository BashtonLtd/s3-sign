from s3sign import parse_args, generate_pre_signed_url, test_url


bucket, key, expires_seconds = parse_args()
head_url = generate_pre_signed_url(bucket, key, expires_seconds, 'head')
test_url(head_url)
get_url = generate_pre_signed_url(bucket, key, expires_seconds, 'get')
print(get_url)
