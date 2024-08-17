from abc import ABC, abstractmethod

class IComponent(ABC):
    @abstractmethod
    def can_operate(self, voltage, temperature):
        pass


class Component(IComponent):
    def __init__(self, name, voltage_range, temperature_range):
        self.name = name
        self.voltage_range = voltage_range
        self.temperature_range = temperature_range
    
    def can_operate(self, voltage, temperature):
        if self.voltage_range is None or self.temperature_range is None:
            return False
        
        min_voltage, max_voltage = self.voltage_range
        min_temp, max_temp = self.temperature_range
        return min_voltage <= voltage <= max_voltage and min_temp <= temperature <= max_temp