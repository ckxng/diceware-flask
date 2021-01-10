import os
import json
from flask import Flask, jsonify, request
from . passphrase import generate

app = Flask(__name__)
app.config.from_mapping(
    DEFAULT_WORDS = int(os.environ.get('DEFAULT_WORDS') or 6),
    DEFAULT_SEPERATOR = os.environ.get('DEFAULT_SEPERATOR') or '-'
)
if app.debug:
    print("DEFAULT_WORDS =",app.config.get("DEFAULT_WORDS"))
    print("DEFAULT_SEPERATOR =",app.config.get("DEFAULT_SEPERATOR"))

@app.route('/api/v1/passphrase')
def passphrase():
    words = app.config.get('DEFAULT_WORDS')
    if request.args.get('words', type=int):
        words = request.args.get('words', type=int)
    
    sep = app.config.get('DEFAULT_SEPERATOR')
    if request.args.get('sep'):
        sep = request.args.get('sep')

    return jsonify({
        'passphrase': generate(words, sep)
    })

if __name__ == "__main__":
    app.run()