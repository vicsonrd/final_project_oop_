class YesButtonSize:
    def __init__(self, size=14):
        self.__size = size  # private attribute

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if size > 0:
            self.__size = size
