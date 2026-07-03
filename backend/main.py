from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from integrations.airtable import authorize_airtable, get_airtable_items
from integrations.notion import authorize_notion, get_notion_items
from integrations.hubspot import authorize_hubspot, get_hubspot_items

app = FastAPI(title="SaaS Integration Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Integration Engine Active"}

@app.post("/integrations/airtable/authorize")
async def airtable_auth(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_airtable(user_id, org_id)

@app.post("/integrations/notion/authorize")
async def notion_auth(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_notion(user_id, org_id)

@app.post("/integrations/hubspot/authorize")
async def hubspot_auth(user_id: str = Form(...), org_id: str = Form(...)):
    return await authorize_hubspot(user_id, org_id)
