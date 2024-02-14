import sys
import uvicorn
from os import getenv

if __name__ == "__main__":
    sys.path.append("src/server")
    port = int(getenv("PORT", 8000))
    uvicorn.run("src.server.app:app", host="0.0.0.0", port=port, reload=True)