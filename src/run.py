import sqlalchemy as sa
import sqlalchemy.orm as so
from microblog import app, db
from microblog.models import User, Post
from microblog import cli


@app.shell_context_processor
def make_shell_context():
    return {"sa": sa, "so": so, "db": db, "User": User, "Post": Post}
