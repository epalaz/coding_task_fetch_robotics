
class BoardSizeException(Exception):

    def __init__(self, message):
        self.message = message


class BoardIndexOutOfBoundsException(Exception):

    def __init__(self, message):
        self.message = message

