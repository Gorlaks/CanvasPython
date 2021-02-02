from pymongo import MongoClient

class DB:
  db = None

  def __init__(self):
    connection_string: str = "localhost:27017"
    client = MongoClient(connection_string)
    self.db = client["Canvas"]

  def ConnectMongoDB(self):
    return self.db

db = DB().ConnectMongoDB()