
"""
Testing Grounds
"""

class Test(object):

    def __init__(self,lst):
        self.list = lst

    @property
    def len(self):
        return len(self.list)

test = Test([1,2,3])
print test.len
test.list = [1,2,3,4]
print test.len

