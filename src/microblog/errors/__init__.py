from flask import Blueprint

bp = Blueprint("errors", __name__)

from microblog.errors import handlers