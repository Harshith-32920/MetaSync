import httpx
import secrets
import base64
import hashlib
from redis_client import set_key_with_ttl, get_key
from integrations.integration_item import IntegrationItem

CLIENT_ID = "AIRTABLE_CLIENT_ID"

async def authorize_airtable(user_id: str, org_id: str):
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode().replace("=", "")
    
    state = f"{user_id}:{org_id}:{secrets.token_hex(16)}"
    set_key_with_ttl(f"airtable_verifier:{state}", code_verifier, ttl=600)

    auth_url = (
        f"https://airtable.com/oauth2/v1/authorize?"
        f"client_id={CLIENT_ID}&response_type=code&state={state}"
        f"&code_challenge={code_challenge}&code_challenge_method=S256"
    )
    return {"auth_url": auth_url}

async def get_airtable_items(credentials: str):
    return [IntegrationItem(id="base_1", name="Airtable Base", type="Base")]
