from core import BaseModel

class AmpType(BaseModel):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Amp Type '{self.name}'"
