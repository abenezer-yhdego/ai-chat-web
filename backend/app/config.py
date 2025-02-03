import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    RATE_LIMIT = "20 per hour"