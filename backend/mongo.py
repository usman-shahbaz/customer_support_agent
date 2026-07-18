from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.customer_support

orders = db.orders


def get_order(order_id):

    return orders.find_one(
        {
            "order_id": order_id
        },
        {
            "_id": 0
        }
    )
