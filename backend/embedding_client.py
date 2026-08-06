import boto3
import json

from config import AWS_REGION, EMBEDDING_MODEL_ID


bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)


def get_embedding(text: str):
    body = json.dumps(
        {
            "inputText": text
        }
    )

    response = bedrock.invoke_model(
        modelId=EMBEDDING_MODEL_ID,
        body=body,
        accept="application/json",
        contentType="application/json",
    )

    response_body = json.loads(response["body"].read())

    return response_body["embedding"]
