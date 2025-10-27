from core import BaseModel
from .amp_types import AmpType


class Amplifier(BaseModel):
    def __init__(self, name: str, amp_type: AmpType, power: int):
        super().__init__(name)
        self.amp_type = amp_type
        self.power = power

    def __repr__(self):
        return f"Amp '{self.name}' - Type: {self.amp_type.name}, Power: {self.power}W"