# # а
# def f(x, h):
#     if x % 10 == 0:
#         return h % 2 == 0
#     elif h == 0:
#         return 0
#     else:
#         if h % 2 != 1:
#             return all([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
#         else:
#             return any([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
# print([i for i in range(11, 100) if i % 10 != 0 and f(i, 2)])

# # б
# def f(x, h):
#     if x % 10 == 0:
#         return h % 2 == 0
#     elif h == 0:
#         return 0
#     else:
#         if h % 2 != 1:
#             return all([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
#         else:
#             return any([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
# print(len([i for i in range(11, 100) if i % 10 != 0 and f(i, 3) and f(i, 1)]))

# # в
# def f(x, h):
#     if x % 10 == 0:
#         return h % 2 == 0
#     elif h == 0:
#         return 0
#     else:
#         if h % 2 != 1:
#             return all([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
#         else:
#             return any([f(x + 1, h - 1), f(x + 3, h - 1), f(x + 11, h - 1)])
# print(sum([i for i in range(11, 100) if i % 10 != 0 and f(i, 4) and not(f(i, 2))]))