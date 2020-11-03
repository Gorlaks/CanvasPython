from ..store.db import db

class AuthRepository:
  user_collection = None

  def __init__(self):
    self.user_collection = db["User"]

  def get_user_data(self, login):
    return self.user_collection.find_one({"login": login})