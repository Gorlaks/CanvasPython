from ..store.db import db

class AuthRepository:
  user_collection = ""

  def __init__(self):
    self.user_collection = db["User"]

  def get_user_data(self):
    return self.user_collection.find_one()["email"]