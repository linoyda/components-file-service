from typing import List
from services.component import IComponent
from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def serve_client(self, filter):
        pass

class FilterService:
    """Given an array of components, filter them according to provided values."""
    def __init__(self, components: List[IComponent]):
        self.components = components
    
    def serve_client(self, filter):
        """The filter in our case is in a format of (int voltage, int temp)."""
        if type(filter) is not tuple:
            return None
        return self.get_filtered_operable_components(filter[0], filter[1])

    def get_filtered_operable_components(self, voltage, temp):
        """Return all opeable components in a specific voltage and temperature value."""

        operable_components = [
            component for component in self.components 
            if component.can_operate(condition=(voltage, temp))
        ]
        return operable_components
