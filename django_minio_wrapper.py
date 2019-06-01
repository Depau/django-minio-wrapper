from minio import Minio
from minio_storage.storage import MinioStorage as DjangoMinioStorage


def MinioStorage(endpoint, access_key, secret_key, bucket_name,
                 secure=True, region=None, *args, **kwargs):
    minio = Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure,
        region=region
    )

    return DjangoMinioStorage(minio, bucket_name, *args, **kwargs)

