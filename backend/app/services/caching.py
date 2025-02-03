import redis
import json
from uuid import uuid4

redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def save_conversation(conversation):
    conversation_id = str(uuid4())
    redis_client.set(conversation_id, json.dumps(conversation), ex=86400)  # Expires in 24 hours
    return conversation_id

def get_conversation(conversation_id):
    conversation = redis_client.get(conversation_id)
    return json.loads(conversation) if conversation else None
