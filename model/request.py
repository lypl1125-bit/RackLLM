from pydantic import BaseModel, Field
from typing import Optional

class RequestModel(BaseModel):
    message: str = Field(..., description="The message to be processed")
    id_agent: str = Field(..., description="The id of the agent")