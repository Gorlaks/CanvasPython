from pymongo import MongoClient

class InitStore:
    __db = "",

    def __init__(self, connection_string):
        client = MongoClient(connection_string)
        self.__db = client["Canvas"]

    def get_database(self):
      return self.__db

    def get_collection(self, title):
      return self.__db[title]

    def ping(self):
      print(1)
