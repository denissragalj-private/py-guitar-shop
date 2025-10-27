from datetime import datetime as dt


class BaseModel:
    """Base class for all models in the application."""
    def __init__(self,
                 name: str,
                 description: str = ""):
        self.name = name
        self.description = description
        self.id = 1
        self.tenant_id = '' # Placeholder for tenant identifier uuid
        self.created_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.created_by = ''
        self.updated_at = dt(1900, 1, 1, 0, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
        self.updated_by = ''
        self.deleted_at = dt(1900, 1, 1, 0, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
        self.deleted_by = ''
        self.is_deleted = False

    def __repr__(self):
        return f"Name '{self.name}', Description '{self.description}'"
