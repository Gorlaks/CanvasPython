from canvas.modules.auth.auth_repository import AuthRepository
from canvas.modules.auth.auth_service import AuthService
from canvas.modules.user.user_repository import UserRepository

class Modules:
    auth_repository = None
    auth_service = None
    user_repository = None

    def __init__(self):
        self.auth_repository = AuthRepository()
        self.auth_service = AuthService()
        self.user_repository = UserRepository()

modules = Modules()
