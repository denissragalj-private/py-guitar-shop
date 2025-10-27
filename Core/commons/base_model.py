import datetime as dt



class BaseModel:
    """Base class for all models in the application."""
    def __init__(self, 
                 name: str,
                 description: str =""):
        self.name = name
        self.description = description
        self.id = 1
        self.tenant_id = '' # placeholder for tenant identifier uuid
        self.created_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.created_by = ''
        self.updated_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_by = ''
        self.deleted_at = dt(1900, 1, 1).strftime("%Y-%m-%d %H:%M:%S"
        self.deleted_by = ''
        self.is_deleted = is_deleted



    def __repr__(self):
        return f"Name '{self.name}', Description '{self.description}'"

    def __str__(self):
        return f"Name '{self.name}'"
    
    def delete(self, deleted_by: str)
        self.is_deleted = True
        self.deleted_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")        
        self.deleted_by = deleted_by