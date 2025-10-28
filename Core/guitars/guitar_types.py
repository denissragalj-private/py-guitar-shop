from core import BaseModel


class GuitarType(BaseModel):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Guitar type '{self.name}'"


# ACOUSTIC = "acoustic"
# ELECTRIC = "electric"
# BASS = "bass"
# CLASSICAL = "classical"
# RESONATOR = "resonator"
# TWELVE_STRING = "12_string"
# SEVEN_STRING = "7_string"
# NINE_STRING = "9_string"
# BARITONE = "baritone"
# MIDI = "midi"
# FRETLESS = "fretless"
# PARLOR = "parlor"
# DREADNOUGHT = "dreadnought"
# JUMBO = "jumbo"
# CONCERT = "concert"
# AUDITORIUM = "auditorium"
# TRAVEL = "travel"
# PARLOR = "parlor"
