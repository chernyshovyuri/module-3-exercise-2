# 3

from __future__ import  annotations

class Size:

    __horizont: float
    __vertic: float

    def __init__(self, horizont: float, vertic: float):

        self.__horizont = horizont
        self.__vertic = vertic


class TopLeftCorner:

    __x: int
    __y: int


    def __init__(self,x: int, y: int):
        self.__x = x
        self.__y = y




class ModelWindow:

    __name: str
    __coordinates: TopLeftCorner
    __size: Size
    __color: str
    __is_viewport: bool
    __is_frame: bool

    def __init__(self, name: str, coordinates: TopLeftCorner, size: Size, color: str, is_viewport: bool, is_frame: bool):
        self.__name = name
        self.__coordinates = coordinates
        self.__size = size
        self.__color = color
        self.__is_viewport = None
        self.__is_frame = None



