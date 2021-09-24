# class Foo:

#     def __init__(self):
#         self.__x = 0

#     @property
#     def x(self):
#         pass

#     @x.getter
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, target):
#         if target is abs(target):
#             digits = list(str(target))
#             self.__x = int("".join(digits[-2:]))
#         else:
#             self.__x = -1



# p = Foo()
# p.x = 135
# print(p.x)


############################################################

# class Foo:
#     def __init__(self):
#         self.__a = 0

#     def get_a(self):
#         return self.__a
    
    
#     @property
#     def set_a(self, a):
#         if a is abs(a):
#             digits = list(str(a))
#             self.__a = int("".join(digits[-2:]))
#         else:
#             self.__a

# p = Foo()
# p.set_a=100
# print(p.get_a())
############################################################

class Foo:
    def __init__(self):
        self.x = 0
        digit = self.x
        if digit > 0:
            digit = list(str(digit))
            self.x = int("".join(digit[-2:]))
        else:
            self.x = 0

    def reza(self):
        digit = self.x
        if digit > 0:
            digit = list(str(digit))
            self.x = int("".join(digit[-2:]))
        else:
            self.x = 0

p = Foo()
p.x = 125
print(p.x)