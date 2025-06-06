
from pydantic import BaseModel, Field
class FloristTag(BaseModel):
    tag: str = Field(..., description="Tag associated with the florist")
