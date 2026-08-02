import boto3

from config import AWS_REGION, CHAT_MODEL_ID

from agent.prompts import SYSTEM_PROMPT
from agent.tool_registry import TOOLS
from agent.tool_executor import ToolExecutor


class CustomerSupportAgent:

    def __init__(self):

        self.bedrock = boto3.client(
            "bedrock-runtime",
            region_name=AWS_REGION,
        )

        self.executor = ToolExecutor()

    def _system_message(self):

        return [
            {
                "text": SYSTEM_PROMPT
            }
        ]

    def chat(
        self,
        question,
        session,
    ):

        messages = session.setdefault(
            "messages",
            []
        )

        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "text": question
                    }
                ]
            }
        )

        while True:

            response = self.bedrock.converse(
                modelId=CHAT_MODEL_ID,
                system=self._system_message(),
                messages=messages,
                toolConfig={
                    "tools": TOOLS
                },
            )

            output = response["output"]["message"]

            stop_reason = response["stopReason"]

            messages.append(output)

            if stop_reason == "end_turn":

                answer = ""

                for item in output["content"]:

                    if "text" in item:
                        answer += item["text"]

                return answer

            if stop_reason != "tool_use":

                return "Unable to process your request."

            tool_result_content = []

            for item in output["content"]:

                if "toolUse" not in item:
                    continue

                tool = item["toolUse"]

                result = self.executor.execute(
                    tool["name"],
                    tool["input"],
                    session,
                )

                tool_result_content.append(
                    {
                        "toolResult": {
                            "toolUseId": tool["toolUseId"],
                            "content": [
                                {
                                    "json": result
                                }
                            ]
                        }
                    }
                )

            messages.append(
                {
                    "role": "user",
                    "content": tool_result_content,
                }
            )
