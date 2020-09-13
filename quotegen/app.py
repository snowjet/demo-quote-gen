import uvicorn

from core.config import LOG_LEVEL

if LOG_LEVEL == "DEBUG":
    DEBUG = "debug"
else:
    DEBUG = "info"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level=DEBUG)
