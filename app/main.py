from flask import Flask

from app.domain.models import db
from app.routes.hero_route import hero_router
import os

app = Flask(__name__)

# init database
db_url = os.getenv("SQLALCHEMY_DATABASE_URI")
if not db_url:
    cwd = os.getcwd()
    db_url = f"sqlite:///{cwd}/db/demo.sqlite3"

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db.init_app(app)

# register blueprints
app.register_blueprint(hero_router, url_prefix="/heros")

@app.route("/")
def check():
    return "Flask is working"


if __name__ == "__main__":
    app.run()
