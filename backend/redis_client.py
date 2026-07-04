import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

def set_key_with_ttl(key: str, value: str, ttl: int = 600):
    redis_client.setex(key, ttl, value)

def get_key(key: str):
    return redis_client.get(key)

def delete_key(key: str):
    redis_client.delete(key)
