from flask import Blueprint, request, jsonify
from app.services.scraper import scrape_website

scrape_bp = Blueprint("scrape", __name__)

@scrape_bp.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    scraped_content = scrape_website(url)
    return jsonify({"content": scraped_content})