# class ThisIsClassPerson:
#     # init - constructs the blueprint for the class. and the atributes the objects will use
#     # self - transportation vehicle for reference of atributes
#
#     def __init__(self, first_name, last_name, age=25):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def say_hi(self):
#         return f'Hello {self.first_name} {self.last_name} on {self.age}'
#
#
# ivan = ThisIsClassPerson('ivan', 'ivanov', 25)
# nikolaj = ThisIsClassPerson("niki", "jordanov", 34)
# print(ivan.say_hi())
# print(nikolaj.say_hi())

# output :
# Hello ivan ivanov on 25
# Hello niki jordanov on 34

class Test:
    def __init__(self, numa, numb):
        self.numa = numa
        self.numb = numb
        self.value = 52

    def sum_numbers(self):
        return self.value + self.numa + self.numb

obj = Test(5, 10)

print(obj.sum_numbers())


