from core import BaseModel


class GuitarType(BaseModel):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)

    def __repr__(self):
        return f"Guitar type '{self.name}'"
