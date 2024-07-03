""" Another way to run the app"""

from src import create_app
import os
from src.config import config

env_name = os.getenv('default')
app = create_app(env_name)

if __name__ == "__main__":
    app.run()