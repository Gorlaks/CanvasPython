from pymongo import MongoClient

class DB:
  def ConnectMongoDB(self):
    connection_string: str = "mongodb+srv://admin:1234@cluster0.wqhlb.azure.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    db = client["Canvas"]
    return db

db = DB().ConnectMongoDB()