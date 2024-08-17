from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def can_operate(self, condition):
        pass


class ElectricComponent(IComponent):
    def __init__(self, name, voltage_range, temp_range):
        self.name = name
        self.voltage_range = voltage_range
        self.temp_range = temp_range
    
    def can_operate(self, condition):
        """Returns whether the component can function in a given voltage and temp values."""
        voltage, temp = condition

        if self.voltage_range is None or self.temp_range is None:
            return False
        
        min_voltage, max_voltage = self.voltage_range
        min_temp, max_temp = self.temp_range
        return min_voltage <= voltage <= max_voltage and min_temp <= temp <= max_temp