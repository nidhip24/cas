"""
This is the __init__.py file for the models package
"""
from src.api.models.user_data import UserData as user_data
from src.api.models.app import App as app
from src.api.models.app_config import AppConfig as app_config
from src.api.models.auth_method import AuthMethod as auth_method
from src.api.models.auth_token import AuthToken as auth_token
from src.api.models.auth_trail import AuthTrail as auth_trail
from src.api.models.auth_user import AuthUser as auth_user
from src.api.models.user_role import UserRole as user_role

__all__ = [
    "app_config",
    "app",
    "auth_method",
    "auth_token",
    "auth_trail",
    "auth_user",
    "user_data",
    "user_role"
]
