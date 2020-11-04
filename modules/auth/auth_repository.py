from ..store.db import db

class AuthRepository:
  """Class for the auth module to get some information about a given user
  
  Main application - To get some data from the User collection of the database

  Attributes
  ----------
  user_collection : User
    dictionary with user data (login, email: Optional, password)

  Methods
  -------
  get_user_data(login)
      Take a data about an user from the collection by the login parametr and
      return data if it is in database otherwise null
  """

  user_collection = None

  def __init__(self):
    self.user_collection = db["User"]

  def get_user_data(self, login: str):
    """Method for getting a data about an user
    
    Parameters
    ----------
    login : str
      login of a needed user
    """

    return self.user_collection.find_one({"login": login})