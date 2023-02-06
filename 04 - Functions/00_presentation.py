# # def even_or_odd_number (num):
# #     if num % 2 == 0:
# #         return ("Even")
# #     else:
# #         return ("Odd")
# # number = int(input())
# #
# # print(even_or_odd_number(number))
#
# numbers = [2, 4, 6, 8, 10]
#
# def squar_number_function(number):
#     return number * number
#
# squar_numbers = list(map(squar_number_function, numbers))
#
# print(squar_numbers)


def header():
    print("This is Header!")


def bottom():
    print("this is bottom ")


def general():
    header()
    bottom()


# recursion

def countdown(number):
    print(number)

    if number == 0:
        return
    else:
        countdown(number - 1)


countdown(9)
