import os
from dotenv import load_dotenv

load_dotenv()
DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
