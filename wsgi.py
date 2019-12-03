from main import app as application
from core.config import LOG_LEVEL

if LOG_LEVEL == "DEBUG":
    DEBUG = True
else:
    DEBUG = False

if __name__ == "__main__":
    application.run(debug=DEBUG, host="0.0.0.0", port=8080)
