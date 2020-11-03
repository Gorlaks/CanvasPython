from ..auth.auth_repository import AuthRepository

class AuthService:
  auth_repository = None

  def __init__(self):
    self.auth_repository = AuthRepository()

  def login(self, login):
    user_data = self.auth_repository.get_user_data(login)
    if (user_data != None):
      response = {
        "id": str(user_data["_id"]),
        "login": user_data["login"],
        "email": user_data["email"]
      }

      return response
    else:
      return "Invalid login"