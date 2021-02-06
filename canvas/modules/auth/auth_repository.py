from canvas.modules.store.db import db
from canvas.models.auth import User

class AuthRepository:
  user_collection = None

  def __init__(self):
    self.user_collection = db["User"]

  def get_user_data(self, login: str) -> User:
    """Method for getting a data about an user
    
    Parameters
    ----------
    login : str
      login of a needed user
    """

    return self.user_collection.find_one({"login": login})