import sqlalchemy as sa
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from app import db
from app.api.errors import error_response
from app.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username,password):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    if user and user.check_password(password):
        return user
    

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)


@token_auth.verify_token
def verify_toke(token):
    return User.check_token() if token else None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)