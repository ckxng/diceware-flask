import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DEFAULT_WORDS = int(os.environ.get('DEFAULT_WORDS') or 6)
    )
    if app.debug:
        print("DEFAULT_WORDS =",app.config.get("DEFAULT_WORDS"))

    return app
