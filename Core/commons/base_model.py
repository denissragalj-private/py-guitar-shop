


class BaseModel:
    """Base class for all models in the application."""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Name '{self.name}'"
