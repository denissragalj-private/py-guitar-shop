from core import BaseModel


class StringType(BaseModel):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"String type '{self.name}'"

# NYLON = "nylon"
# STEEL = "steel"
# BRONZE = "bronze"
# COATED = "coated"
# FLATWOUND = "flatwound"
# ROUNDED = "rounded"
