from core import BaseModel
from .guitar_types import GuitarType


class Guitar(BaseModel):
    def __init__(self, name: str, guitar_type: GuitarType, number_of_strings: int):
        super().__init__(name)
        self.guitar_type = guitar_type
        self.number_of_strings = number_of_strings

    def __repr__(self):
        return f"Guitar {self.name} ({self.guitar_type}, {self.number_of_strings} strings)"