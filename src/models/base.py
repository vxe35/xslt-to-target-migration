from typing import Any

from pydantic import BaseModel

class Base(BaseModel):
    id: int
    created_at: Any
    updated_at: Any