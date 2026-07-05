from pydantic import BaseModel
from typing import Optional, List

class IntegrationItem(BaseModel):
    id: str
    name: str
    type: str
    parent_id: Optional[str] = None
    children: Optional[List['IntegrationItem']] = []

IntegrationItem.update_forward_refs()
