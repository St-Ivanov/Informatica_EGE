# def f(x, y, h):
#     if x + y >= 227 and h == 3:
#         return 1
#     elif x + y < 227 and h == 3:
#         return 0
#     elif x + y >= 227 and h < 3:
#         return 0
#     else:
#         if h % 2 != 0:
#             return any([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
#         else:
#             return any([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
# for i in range(1, 210):
#     if f(17, i, 1):
#         print(i)
#         break
# # 53

# def f(x, y, h):
#     if x + y >= 227 and h == 4:
#         return 1
#     elif x + y < 227 and h == 4:
#         return 0
#     elif x + y >= 227 and h < 4:
#         return 0
#     else:
#         if h % 2 != 0:
#             return any([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
#         else:
#             return all([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
# for i in range(1, 210):
#     if f(17, i, 1):
#         print(i)
# # 96 104

# def f(x, y, h):
#     if x + y >= 227 and (h == 5 or h == 3):
#         return 1
#     elif x + y < 227 and h == 5:
#         return 0
#     elif x + y >= 227 and h < 5:
#         return 0
#     else:
#         if h % 2 != 0:
#             return all([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
#         else:
#             return any([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
# def f1(x, y, h):
#     if x + y >= 227 and h == 3:
#         return 1
#     elif x + y < 227 and h == 3:
#         return 0
#     elif x + y >= 227 and h < 3:
#         return 0
#     else:
#         if h % 2 != 0:
#             return all([f1(x + 1, y, h + 1), f1(x * 2, y, h + 1), f1(x, y + 1, h + 1), f1(x, y * 2, h + 1)])
#         else:
#             return any([f1(x + 1, y, h + 1), f1(x * 2, y, h + 1), f1(x, y + 1, h + 1), f1(x, y * 2, h + 1)])

# for i in range(1, 210):
#     if f(17, i, 1):
#         print(1, i)
#     if f1(17, i, 1):
#         print(2, i)
# # 95