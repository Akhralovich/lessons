rom flask import Flask

from sqlalchemy import create_engine

from lesson_13.utils import create_tables
from lesson_13.models import User

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
   users = app.session.query(User).all()
   return [u.as_dict() for u in users]


if __name__ == "__main__":
   engine = create_engine("postgresql://manti:manti@localhost/manti")
   app.session = create_tables(engine)
   app.run()
