from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from __seedwork.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class Category(Entity):

    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now())

    def _update_name(self, name: str):
        object.__setattr__(self, 'name', name)

    def _update_description(self, description: str):
        object.__setattr__(self, 'description', description)

    def update(self, name: str, description: Optional[str] = None):
        self._update_name(name)
        self._update_description(description)

    def activate(self):
        object.__setattr__(self, 'is_active', True)

    def deactivate(self):
        object.__setattr__(self, 'is_active', False)
