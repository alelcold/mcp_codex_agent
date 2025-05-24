from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("MCP_CLI_API", "http://localhost:8000")
