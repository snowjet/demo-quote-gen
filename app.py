from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from six.moves.urllib.parse import urlencode

from core.config import LOG_LEVEL
from core.log import logger
from core.quote_gen import quote_gen

logger.info("Config Imported", LOG_LEVEL=LOG_LEVEL)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = Flask(__name__)

@app.route('/')
def home():
    name, quote = quote_gen()
    return jsonify(name=name,
                   quote=quote)

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)
