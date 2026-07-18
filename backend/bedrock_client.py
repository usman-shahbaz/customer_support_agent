import boto3

from config import (
    AWS_REGION,
)

bedrock = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION,
)


def client():
    return bedrock
