from flask import Blueprint, request, jsonify
from app.services.caching import save_conversation, get_conversation

share_bp = Blueprint("share", __name__)

@share_bp.route("/share", methods=["POST"])
def share():
    data = request.json
    conversation_id = save_conversation(data)
    return jsonify({"share_link": f"/conversation/{conversation_id}"})

@share_bp.route("/conversation/<conversation_id>", methods=["GET"])
def get_shared_conversation(conversation_id):
    conversation = get_conversation(conversation_id)
    if not conversation:
        return jsonify({"error": "Conversation not found"}), 404

    return jsonify({"conversation": conversation})
