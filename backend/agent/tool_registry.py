TOOLS = [
    {
        "toolSpec": {
            "name": "search_company_knowledge",
            "description": "Search company knowledge base for shipping, return policy, warranty, address, payment methods, FAQs and company information.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "question"
                    ]
                }
            }
        }
    },
    {
        "toolSpec": {
            "name": "get_order_details",
            "description": "Retrieve customer order details using an order id.",
            "inputSchema": {
                "json": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "question"
                    ]
                }
            }
        }
    }
]
