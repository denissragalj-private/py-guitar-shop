from core import BaseModel


class GuitarType(BaseModel):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Guitar type '{self.name}'"
