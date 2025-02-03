from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
import redis

# Flask App Factory
def create_app():
    app = Flask(__name__)

    # Load Configuration
    app.config.from_object("app.config.Config")

    # Enable CORS
    CORS(app)

    # Intialize Rate Limiting
    limiter = Limiter(
        key_func=get_remote_address,
        storage_uri="redis://localhost:6379/1",  # Using Redis database 1 for rate limiting
    )


    # Initialize Caching (Redis)
    cache = Cache(app, config={"CACHE_TYPE": "RedisCache", "CACHE_REDIS_URL": "redis://localhost:6379/0"})

    # Import and Register Blueprints (Routes)
    from app.routes.chat_routes import chat_bp
    from app.routes.scrape_routes import scrape_bp
    from app.routes.share_routes import share_bp

    app.register_blueprint(chat_bp)
    app.register_blueprint(scrape_bp)
    app.register_blueprint(share_bp)

    return app