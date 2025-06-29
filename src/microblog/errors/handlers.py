from flask import render_template
from microblog import db
from microblog.errors import bp
from sqlalchemy.exc import InvalidRequestError


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    try:
        db.session.rollback()
    except InvalidRequestError:
        pass
    return render_template("errors/500.html"), 500
