import sys
import uvicorn
from os import getenv

if __name__ == "__main__":
    sys.path.append("server")
    port = int(getenv("PORT", 10000))
    uvicorn.run("server.app:app", host="0.0.0.0", port=port, reload=True)