from abc import ABC, abstractmethod
import re

class IParser(ABC):
    @abstractmethod
    def parse_data(self):
        pass


class TextToComponentParser(IParser):
    VOLTAGE_PATTERN = r"(\d+(\.\d+)?)V to (\d+(\.\d+)?)V"  # TBD, not perfect, not catching floats
    TEMPERATURE_PATTERN = r"(-?\d+)°C to (-?\d+)°C"  # TBD

    def __init__(self, file_content_dict):
        self.file_content_dict = file_content_dict
    
    def __check_consistency(self, matches):
        ranges = [(float(match[0]), float(match[2])) for match in matches]
        if len(set(ranges)) == 1:  # All ranges are the same
            return ranges[0]
        return None  # Inconsistent ranges

    def parse_data(self):
        """For each filename, create a component with the required information."""
        components = []

        voltage_matches = re.findall(self.VOLTAGE_PATTERN, self.file_content)
        temperature_matches = re.findall(self.TEMPERATURE_PATTERN, self.file_content)
        
        voltage_range = self.__check_consistency(voltage_matches)
        temperature_range = self.__check_consistency(temperature_matches)
        
        return components