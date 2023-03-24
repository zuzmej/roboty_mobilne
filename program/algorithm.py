from abc import ABC, abstractmethod
from data import data

class algorithm(data,ABC):
    
    @abstractmethod
    def solve(self):
        pass
