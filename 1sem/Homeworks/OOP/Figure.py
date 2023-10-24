from abc import ABC, abstractmethod
import pandas as pd

class Figure(ABC):
    def __init__(self, points: tuple[tuple, ...]):
        self.__points = points
        self.__square = self.calculateSquare()
        self.__perimeter = self.calculatePerimeter()
        
    @abstractmethod
    def calculatePerimeter(self) -> float:
        pass

    @abstractmethod
    def calculateSquare(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    @classmethod
    def constructFromSeries(series: pd.Series) -> object:
        """construct instance from pandas.Series"""

    @abstractmethod
    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        pass


