from core import BaseModel


class GuitarType(BaseModel):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Guitar type '{self.name}'"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
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
