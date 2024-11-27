# Get the database using the methond we defined in pymongo_test_insert file

from ..pymongo_get_database import get_database

from dateutil import parser

# retrieves the database
dbname = get_database()

# adds a collection to the database
collection_name = dbname["user_1_items"]

# test sample dates
expiry_date = '2024-12-01'
expiry = parser.parse(expiry_date)

# inserting items

item_1 = {
    "_id" : "UIT0001",
    "item_name" : "Blender",
    "max_discount" : "10%",
    "batch_number" : "RR4500FRG",
    "price" : 340,
    "category" : "kitchen appliance"
}

item_2 = {
    "_id" : "UIT0002",
    "item_name" : "Egg",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "brown country eggs"
}

item_3 = {
    "item_name" : "Bread",
    "quantity" : 2,
    "ingredients" : "all-purpose flour",
    "expiry_date" : expiry
}

collection_name.insert_one(item_3)
#collection_name.insert_many([item_1, item_2])