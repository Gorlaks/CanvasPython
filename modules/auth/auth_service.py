from typing import Dict

from .auth_repository import AuthRepository
from ...models.auth import User

class AuthService:
  """Class for the auth module to proccess an information
  received from the auth repository and return it to the client.
  
  Attributes
  ----------
  auth_repository : AuthRepository
    Class for getting some information about an user
  user_collection : MongoDB User Collection
    Collection of users from database

  Methods
  -------
  login(login)
    Method for processing received user data and return it to the client
  registration(user_data)
    Method for user registration
  """

  auth_repository = None
  user_collection = None

  def __init__(self):
    self.auth_repository = AuthRepository()

  def login(self, login: str) -> Dict[str, str]:
    """Proccess user data and return it otherwise
    error
    
    Parameters
    ----------
    login : str
      login of an user
    """

    user_data: User = self.auth_repository.get_user_data(login)
    if (user_data != None):
      response = {
        "id": str(user_data["_id"]),
        "login": user_data["login"],
        "email": user_data["email"]
      }

      return response
    else:
      return {
        "code": "0",
        "message": "Invalid login"
      }

  
  def registration(self, user_data: User):
    """User registration
    
    Parameters
    ----------
    user_data : User
      Dictionary with an user data (login, email: Optional, password)
    """

    return ""
