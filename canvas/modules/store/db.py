from pymongo import MongoClient

class DB:
  def ConnectMongoDB(self):
    connection_string: str = "localhost:27017"
    client = MongoClient(connection_string)
    db = client["Canvas"]
    return db

db = DB().ConnectMongoDB()