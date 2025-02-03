from flask import Blueprint, request, jsonify
from app.services.llm_service import get_llm_response

chat_bp = Blueprint("chat",__name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    context = data.get("context", "")

    if not user_input:
        return jsonify({"error": "Messgae is required"}), 400
    
    response = get_llm_response(user_input, context)
    return jsonify({"response": response})
