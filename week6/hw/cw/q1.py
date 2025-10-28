​class Victor3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
    @property
    def x(self):
        return self.__x
    @x.setter
    def x (self, value):
        self.__x = value
    @property
    def y(self):
        #self.__y = value
        return self.__y
    @y.setter
    def y (self, valeu):
        self.__y = valeu
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, value):
        self.__z = value

    def __add__ (self, other):
        return Victor3d(self.__x +other.x,  self.__y+other.y, self.__z+other.z, )
    def __sub__ (self, other):
        return Victor3d(self.__x -other.x, - self.__y-other.y, -self.__z+other.z, )

    def __iadd__ (self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __radd__ (self, other):
     if isinstance(other,(int,float)):
         return Victor3d(self.__x+other, self.__y+other, self.__z+other)


    def __eq__ (self , other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __len__ (self):
        return 3
    def __str__(self):
        return f"Victor x={self.x}, y={self.y}, z={self.z}"
    def __repr__(self):
        return f"Victor x={self.x}, y={self.y}, z={self.z}"

v1 = Victor3d(0, 0, 0)
v2 = Victor3d(1, 2, 3)
v3 = Victor3d(4, 5, 6)
print(v1)
print(v2)
print(v3)
print(v1 + v2)
print(v1 - v2)
print(10 +v2)
print(v2 == v3)
print(len(v1))