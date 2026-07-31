from tools.company_search import search_company_knowledge
from tools.order_lookup import get_order_details


class ToolExecutor:

    def execute(
        self,
        tool_name,
        tool_input,
        session,
    ):

        if tool_name == "search_company_knowledge":

            return search_company_knowledge(
                tool_input["question"]
            )

        if tool_name == "get_order_details":

            return get_order_details(
                tool_input["question"],
                session,
            )

        return {
            "success": False,
            "message": "Unknown tool."
        }
