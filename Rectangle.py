class Rectangle:
    def __init__(self,length:int, width:int):
        self.length = length
        self.width = width
    def __iter__(self):
        yield {'length' : self.length }
        yield {'width' : self.width}

instance = Rectangle(10,20)
for i  in instance:
    print(i)
