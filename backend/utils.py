import re

ORDER_PATTERN = r"(ORD|ord)[0-9]+"


def extract_order_id(text):

    match = re.search(ORDER_PATTERN, text)

    if match:
        return match.group().upper()

    return None
