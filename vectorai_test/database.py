import logging

from astrapy import DataAPIClient
from astrapy.data.info.collection_descriptor import CollectionDefinition

import constant

def getDatabaseConnection():
    try:
        # Instantiate the client
        client = DataAPIClient()

        # Connect to a database
        database = client.get_database(constant.vector_db_endpoint, token=constant.vector_db_token)
        return database,""

    except Exception as e:
        logging.info("Some Exception Occurred while creating connection")
        return "",str(e)



def createDbEntry(tableName,param):
    try:
        database = getDatabaseConnection()
        collection = database.create_collection(
            tableName,
            definition=CollectionDefinition.builder().set_vector_dimension(5).build(),
        )
        collection.insert_one({
            "title": param.title,
            "$vector": param.vector,
        })

        return "DB Save Successfull",""

    except Exception as e:
        logging.info("Exception Occured while DB Save")
        return "",str(e)








# Get an existing collection
#collection = database.get_collection("COLLECTION_NAME")

# Use vector search and filters to find a document
# result = collection.find_one(
#     {
#         "$and": [
#             {"is_checked_out": False},
#             {"number_of_pages": {"$lt": 300}},
#         ]
#     },
#     sort={"$vectorize": "A thrilling story set in a futuristic world"},
# )

#print(result)