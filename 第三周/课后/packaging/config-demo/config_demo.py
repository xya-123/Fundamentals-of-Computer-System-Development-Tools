import os

mode = os.getenv("APP_MODE", "development")
port = int(os.getenv("APP_PORT", "8000"))
debug = os.getenv("DEBUG", "false").lower() == "true"

print(f"mode={mode}")
print(f"port={port}")
print(f"debug={debug}")