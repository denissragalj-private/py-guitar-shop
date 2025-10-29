from core import BaseModel
from .guitar_types import GuitarType


class Guitar(BaseModel):
    def __init__(self, name: str, guitar_type: GuitarType, number_of_strings: int):
        super().__init__(name)
        self.guitar_type = guitar_type
        self.number_of_strings = number_of_strings

    def __repr__(self):
        return f"Guitar {self.name} ({self.guitar_type}, {self.number_of_strings} strings)"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "guitar_type": self.guitar_type.to_dict(),
            "number_of_strings": self.number_of_strings,
            "description": self.description,
            "tenant_id": self.tenant_id,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "updated_at": self.updated_at,
            "updated_by": self.updated_by,
            "deleted_at": self.deleted_at,
            "deleted_by": self.deleted_by,
            "is_deleted": self.is_deleted
        }
