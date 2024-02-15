import sys
import uvicorn
from os import getenv

if __name__ == "__main__":
    sys.path.append("server")
    port = int(getenv("PORT", 8000))
    uvicorn.run("server.app:app", host="localhost", port=port, reload=True)