from fastapi.responses import JSONResponse
from typing import Dict
import datetime
import pytz

from canvas.modules.store.db import db
from canvas.modules.auth.auth_repository import AuthRepository
from canvas.models.auth import User
from canvas.utils.hashing import hash_password
from canvas.utils.helpers import destruct_dict
from canvas.utils.data import default_response_to_client

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
    self.user_collection = db["User"]

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
      default_response_to_client["message"] = "Invalid login"
      return JSONResponse(status_code=404, content=default_response_to_client)

  
  def registration(self, user_data: User) -> Dict[str, str]:
    """User registration
    
    Parameters
    ----------
    user_data : User
      Dictionary with an user data (login, email: Optional, password)
    """

    email, login, password = destruct_dict(user_data)

    if login == "":
      default_response_to_client["message"] = "Login is empty"
      return JSONResponse(status_code=404, content=default_response_to_client)
    if password == "":
      default_response_to_client["message"] = "Password is empty"
      return JSONResponse(status_code=404, content=default_response_to_client)

    user_data.password = hash_password(user_data.password)
    registration_date = datetime.datetime.now(pytz.timezone('Europe/Moscow'))

    inserted_id = self.user_collection.insert_one({
      "email": user_data.email,
      "login": user_data.login,
      "password": user_data.password,
      "registration date": registration_date
    }).inserted_id

    if inserted_id != None:
      default_response_to_client["code"] = "0"
      default_response_to_client["message"] = "Success"
      return default_response_to_client
    else:
      return default_response_to_client