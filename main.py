from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from six.moves.urllib.parse import urlencode

from core.config import LOG_LEVEL, QUOTE_BACKEND
from core.log import logger
from core.quote import get_quote

logger.info("Config Imported", LOG_LEVEL=LOG_LEVEL)

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

app = Flask(__name__)

if QUOTE_BACKEND == 'DB':
    from db.db_utils import load_schema_safe
    msg = load_schema_safe()
    logger.info("Setup DB", load_schema_msg=msg)

@app.route("/")
def home():
    name, quote = get_quote()
    logger.info("Returned Quote:", author=name, quote=quote)
    return jsonify(name=name, quote=quote, backend=backend)


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8080)
