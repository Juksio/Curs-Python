print("Hello World")
# # # # for x in [1, 2, 3]:
# # # #     print(x)
# # # #     print(x==2)
# # # #
# # # # print("Ma numesc:\n\"Razvan\"")
# # # #
# # # #
# # # # print('ada\nare mare')
# # # #
# # # #
# # # # name = "Razvan"
# # # # age = 23
# # # # print(f"ma numesc {name} si am {age} ani")
# # # #
# # # #
# # # # l = [1, 2, 3, 4, 5, 9]
# # # # m = [2, 3, 1]
# # # #
# # # # m[0] = 99
# # # # print(l == m)
# # # # print(l)
# # # # print(m)
# # # #
# # # # second_name = "M" + name
# # # # print(second_name)
# # # #
# # # # max = len(l)
# # # # print(max)
# # # # print(l[max-1])
# # # #
# # # # print(l[-1])
# # # #
# # # #
# # # # l1 = [1, 2, 3]
# # # # l2 = [4, 5, 6]
# # # #
# # # # l0 = l1 + l2
# # # # print(l0)
# # # #
# # # # l1.extend(l2)
# # # # print(l1)
# # # # print(l2)
# # # #
# # # #
# # # # d = {
# # # #     'x': 100,
# # # #     'y': 200
# # # # }
# # # #
# # # # print(d['x'])
# # # # print(d['y'])
# # # #
# # # # print(d.get('z', 0))
# # # #
# # # # g = d
# # # #
# # # # d['x'] = 900
# # # # print(g)
# # # #
# # # #
# # # #
# # # # l1 = [1, 2, 3, 3, 1, 4, 5]
# # # #
# # # # s1 = set(l1)
# # # # print(s1)
# # # # print(list(s1))
# # # #
# # # #
# # # # s1 = {1, 2, 3, 4, 5}
# # # # s2 = {2, 3}
# # # # print(s2.issubset(s1))
# # # #
# # # #
# # # #
# # # #
# # # # my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# # # # print(my_list)
# # # # print(sorted(my_list))
# # # # my_sliced_list = my_list[1::2]
# # # # print(my_sliced_list)
# # # # my_sliced_list = my_list[::2]
# # # # print(my_sliced_list)
# # # # for i in range(len(my_list)):
# # # #     if my_list[i]%3 == 0:
# # # #         print(my_list[i])
# # #
# # # for i in range(1, 10):
# # #     for j in range(5):
# # #         print(j, end=' ')
# # #     print()
# # #     # print(i)
# #
# #
# # for i in range(10):
# #     for j in range(5):
# #         print(i, end=' ')
# #         print(j, end='')
# # print()
# #
# import random
#
# avaible_choice = range(11)
# while True:
#     random_choice = random.choice(avaible_choice)
#     if random_choice % 3 == 0:
#         break
#     print(f'randome choice is {random_choice}')
#
# print(f'Exit random choice is {random_choice}')
#
# for i in avaible_choice:
#     if i % 2 != 0:
#         continue
#     print(f'i is even: {i}')
#


def my_function(list_param):
    list_param.append(4)


my_list = [1, 2, 3]
my_function(my_list)
print((my_list))


def my_second_function(p1, p2, *args, p3=0, **kwargs):
    print(p1)
    print(p2)

    for arg in args:
        print(arg)

    print(p3)
    for kwarg in kwargs:
        print(kwargs[kwarg])

my_second_function(1, 2, 99, 100, p3='3', p4='4', p5='5')
