import datetime as dt



class BaseModel:
    """Base class for all models in the application."""
    def __init__(self, 
                 id: int, 
                 name: str,
                 description: str ="",
                 created_at: str = "",
                 created_by: str = "",
                 updated_at: str = "",
                 updated_by: str = "",
                 deleted_at: str = "",
                 deleted_by: str = "",
                 # Soft delete flag
                 is_deleted: bool = False):
        
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.deleted_at = deleted_at
        self.deleted_by = deleted_by
        self.is_deleted = is_deleted


    def __repr__(self):
        return f"Name '{self.name}', Description '{self.description}'"

    def __str__(self):
        return f"Name '{self.name}'"
    
    def delete(self, deleted_by: str)
        self.is_deleted = True
        self.deleted_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")        
        self.deleted_by = deleted_by