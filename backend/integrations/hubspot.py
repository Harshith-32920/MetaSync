import httpx
from integrations.integration_item import IntegrationItem

async def authorize_hubspot(user_id: str, org_id: str):
    auth_url = "https://app.hubspot.com/oauth/authorize?client_id=HUBSPOT_ID&scope=crm.objects.contacts.read"
    return {"auth_url": auth_url}

async def get_hubspot_items(credentials: str):
    return [IntegrationItem(id="contact_1", name="HubSpot Contacts", type="ContactList")]
