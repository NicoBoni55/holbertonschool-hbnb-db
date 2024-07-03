""" Another way to run the app"""

from src import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hbnb.db"
app.config["SQLALCHEM_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

if __name__ == "__main__":
    app.run()