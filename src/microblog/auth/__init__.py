from flask import Blueprint

bp = Blueprint("auth", __name__)

from microblog.auth import routes
