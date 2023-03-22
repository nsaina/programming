class Point:
    MIN_COORD=0
    MAX_COORD=100
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_cord(self,x,y):
        if self.MIN_COORD<=x<=self.MAX_COORD:
            self.x=x
            self.y=y
    def __getattribute__(self, item):
        if item=="x":
            # запретили обращаться к атрибуту х
            raise ValueError("доступ запрещен")
        else:
            '''Например создадим экземпляр класса 
            pt1=Point(1,2)
            a=pt1.x
            print(a) будет возвращать ValueError тк обращение к х запрещен'''
            return object.__getattribute__(self,item)
    def __setattr__(self, key, value):
    #вызывается при создании экземпляра класса, именно когда происходит
    #присвоение значений к атрибуту например при self.x=x в методе __init__
        if key=='z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self,key,value)
    def __getattr__(self, item):
    #вызывается когда происходит обращение к несуществующему атрбуту класса
        print("__getattr__"+ item)

    def __delattr__(self, item):
    #вызывается при удалении атрибута
        print("__delattr__: "+item)
        #без этой строчки атрибут не удаляется, но все равно происходит вызов данной функции
        object.__delattr__()
pt1=Point(1,2)
pt2=Point(3,7)