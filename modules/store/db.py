from pymongo import MongoClient

connection_string: str = "mongodb+srv://admin:1234@cluster0.wqhlb.azure.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["Canvas"]