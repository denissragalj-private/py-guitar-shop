from core import BaseModel

class AmpType(BaseModel):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)

    def __repr__(self):
        return f"Amp Type '{self.name}'"
