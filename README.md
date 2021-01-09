# diceware-flask

## Development
Run the following commands to setup your Python environment.

    python -m venv venv
    pip install -r requirements.txt
    cp default.env .env

## Environment File
Set environment variables in `.env`

    FLASK_APP=diceware
    FLASK_ENV=development
    FLASK_DEBUG=0

Set the Flask environment variables.  FLASK_APP is required.

    DEFAULT_WORDS=8

Set the number of words to be included in passphrases by default.
