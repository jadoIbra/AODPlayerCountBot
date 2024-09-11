# settings.py 
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
SERVER_API_SECRET = os.getenv('SERVER_API_RESPONSE')