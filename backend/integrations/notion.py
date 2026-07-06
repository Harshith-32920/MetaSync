import httpx
from integrations.integration_item import IntegrationItem

def _recursive_dict_search(d: dict, target_key: str):
    if target_key in d:
        return d[target_key]
    for k, v in d.items():
        if isinstance(v, dict):
            item = _recursive_dict_search(v, target_key)
            if item is not None:
                return item
    return None

async def authorize_notion(user_id: str, org_id: str):
    auth_url = "https://api.notion.com/v1/oauth/authorize?client_id=NOTION_ID&response_type=code"
    return {"auth_url": auth_url}

async def get_notion_items(credentials: str):
    return [IntegrationItem(id="page_1", name="Notion Root Page", type="Page")]
