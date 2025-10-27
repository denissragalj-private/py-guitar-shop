from core import BaseModel, StringType


class GuitarString(BaseModel):
    def __init__(self, name: str, gauge: float, type: StringType):
        super().__init__(name)
        self.gauge = gauge  # in inches
        self.type = type  # e.g., 'nylon', 'steel', 'bronze'

    def __repr__(self):
        return f"Guitar String {self.name} ({self.gauge} / {self.type})"

    def tension(self, frequency: float, scale_length: float) -> float:
        """
        Calculate the tension of the string using the formula:
        T = (4 * L^2 * f^2 * m) / g
        where:
        T = tension in Newtons
        L = scale length in meters
        f = frequency in Hz
        m = mass per unit length in kg/m
        g = gravitational acceleration (9.81 m/s^2)

        For simplicity, we will assume a constant mass per unit length based on gauge.
        """
        g = 9.81  # m/s^2
        # Approximate mass per unit length (kg/m) based on gauge (inches)
        mass_per_unit_length = self.gauge * 0.0005  # This is a simplification

        L_meters = scale_length / 1000  # Convert mm to meters
        T = (4 * L_meters**2 * frequency**2 * mass_per_unit_length) / g
        return T
