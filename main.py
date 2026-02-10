# 3

from __future__ import  annotations

class Size:

    __horizont: float
    __vertic: float

    def __init__(self, horizont: float, vertic: float):

        self.__horizont = horizont
        self.__vertic = vertic


    def __get_horizont(self):
        return self.__horizont

    def __get_vertic(self):
        return self.__vertic

    def __set_horizont(self, new_horizont: float) -> float | bool:

        if new_horizont < 0 or new_horizont > 1960 or new_horizont is None:  return False

        self.__horizont = new_horizont

        return True

    def __set_vertic(self, new_vertic: float) -> float | bool:

        if new_vertic < 0 or new_vertic > 1080 or new_vertic is None:  return False

        self.__vertic = new_vertic

        return True

    horizont = property(__get_horizont, __set_horizont)
    vertic = property(__get_vertic, __set_vertic)



class TopLeftCorner:

    __x: int
    __y: int


    def __init__(self,x: int, y: int):
        self.__x = x
        self.__y = y

    def __get_x(self):
        return self.__x


    def __get_y(self):
        return self.__y


    def __set_x(self, new_x: int) -> int | bool:


        if new_x < 0 or new_x > 1960 or new_x is None:  return False

        self.__x = new_x
        return True


    def __set_y(self, new_y: int) -> int | bool:

        if new_y < 0 or new_y > 1080 or new_y is None: return False

        self.__y = new_y
        return True

    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)



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
        self.__is_viewport = is_viewport
        self.__is_frame = is_frame



    def get_name(self):
        return self.__name

    def get_coordinates(self):
        return self.__coordinates

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def __str__(self):
        return f'Name: {self.__name}\nCoordinates: {self.__coordinates}\nSize: {self.__size}'


    def active(self):
        self.__is_viewport == True

    def not_active(self):
        self.__is_viewport == False


    def moving_horizont(self, new_horizont: float):

        self.__coordinates.x = new_horizont

    def moving_vertict(self, new_vertic: float):

        self.__coordinates.y = new_vertic


    def resizing(self, new_horizont: int, new_vertic: int):

        self.__size.horizont = new_horizont

        self.__size.vertic = new_vertic

    def set_color(self, new_color: str):

        self.__color = new_color


    def status(self):

        self.__is_viewport = False if self.__is_viewport else True














