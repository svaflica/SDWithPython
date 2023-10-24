from abc import ABC, abstractmethod

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
    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        pass



def constructFromDataSeries(series) -> Figure:
    """
    Return one of the ```Figure``` children classes instance constructed from pandas data series ```series``` where specified
    type of the figure, neccessary points (such as center and radius for circle, axes for ellipse e.t.c.)
    """

