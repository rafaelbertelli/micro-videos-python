from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Category:
    
    name:str
    description:Optional[str] = None
    is_active:Optional[bool] = True
    created_at:Optional[datetime] = datetime.now()
    
