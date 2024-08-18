from abc import ABC, abstractmethod
from services.component import ElectricComponent
import re

class IParser(ABC):
    @abstractmethod
    def parse_data(self):
        pass


class TextToComponentParser(IParser):
    VOLTAGE_REGEX = r"(\d+(\.\d+)?)\s*V\s*(?:to|TO|To|tO)\s*(\d+(\.\d+)?)\s*V"
    TEMP_REGEX = r"(-?\d+(\.\d+)?)\s*°\s*C\s*(?:to|TO|To|tO)\s*(\+?-?\d+(\.\d+)?)\s*°\s*C"

    def __init__(self, file_content_dict):
        self.file_content_dict = file_content_dict
    
    def __check_consistency(self, matches):
        ranges = [(float(match[0]), float(match[1])) for match in matches]
        if len(set(ranges)) == 1:  # set automatically reduces duplicates.
            return ranges[0]
        return None  # Inconsistent ranges

    def parse_data(self):
        """For each filename, create a component with the required information."""
        components = []

        for file_name, content in self.file_content_dict.items():
            try:
                if not file_name or not content:
                    continue
                
                # filter subgroups
                voltage_matches = [(match[0], match[2]) for match in re.findall(self.VOLTAGE_REGEX, content)]
                temp_matches = [(match[0], match[2]) for match in re.findall(self.TEMP_REGEX, content)]
                
                voltage_range = self.__check_consistency(voltage_matches)
                temp_range = self.__check_consistency(temp_matches)

                components.append(ElectricComponent(file_name, voltage_range, temp_range))
            except:
                print("failed parsing content from file: " + file_name)
        
        return components