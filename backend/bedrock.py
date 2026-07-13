import boto3
from dotenv import load_dotenv


load_dotenv()

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


def get_response(messages):
    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=messages
    )

    return response["output"]["message"]["content"][0]["text"]
