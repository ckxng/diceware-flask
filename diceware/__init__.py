import os
import json
from flask import Flask, jsonify
from . passphrase import generate

app = Flask(__name__)
app.config.from_mapping(
    DEFAULT_WORDS = int(os.environ.get('DEFAULT_WORDS') or 6)
)
if app.debug:
    print("DEFAULT_WORDS =",app.config.get("DEFAULT_WORDS"))

@app.route('/api/v1/passphrase')
def passphrase():
    return jsonify({
        'passphrase': generate(app.config.get('DEFAULT_WORDS'))
    })

if __name__ == "__main__":
    app.run()