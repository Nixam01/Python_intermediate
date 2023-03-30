class BITException(Exception):
    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

try:
    # do something...
    raise BITException("file format is incorrect", "Financial data")
except BITException as e:
    print("Application error: {}, area {}".format(e,e.area))

try:
    # do something...
    raise BITException("file format is incorrect", "HR data")
except BITException as e:
    print("Application error: {}, area {}".format(e,e.area))