import uvicorn
import os

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
if LOG_LEVEL not in ["INFO", "DEBUG"]:
    LOG_LEVEL = "INFO"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level=LOG_LEVEL.lower())
