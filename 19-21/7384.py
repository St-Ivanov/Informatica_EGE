# # 1
# def f(x, h):
#     if h == 2 and x >= 61:
#         return 1
#     elif h == 2 and x < 61:
#         return 0
#     elif h < 2 and x >= 61:
#         return 0
#     else:
#         if x * 2 <= 80:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#             else:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#         else:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1)
#             else:
#                 return f(x + 1, h + 1)
# ans = []
# for x in range(1, 61):
#     if f(x, 1):
#         ans.append(x)
# print(len(ans))
# 11

# # 2
# def f(x, h):
#     if h == 4 and x >= 61:
#         return 1
#     elif h == 4 and x < 61:
#         return 0
#     elif h < 4 and x >= 61:
#         return 0
#     else:
#         if x * 2 <= 80:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#             else:
#                 return f(x + 1, h + 1) and f(x * 2, h + 1)
#         else:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1)
#             else:
#                 return f(x + 1, h + 1)
# for x in range(1, 61):
#     if f(x, 1):
#         print(x)
# # 15 29

# # 3
# def f(x, h):
#     if (h == 3 or h == 5) and x >= 61:
#         return 1
#     elif h == 5 and x < 61:
#         return 0
#     elif h < 5 and x >= 61:
#         return 0
#     else:
#         if x * 2 <= 80:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1) and f(x * 2, h + 1)
#             else:
#                 return f(x + 1, h + 1) or f(x * 2, h + 1)
#         else:
#             if h % 2 != 0:
#                 return f(x + 1, h + 1)
#             else:
#                 return f(x + 1, h + 1)


# def f1(x, h):
#     if h == 3 and x >= 61:
#         return 1
#     elif h == 3 and x < 61:
#         return 0
#     elif h < 3 and x >= 61:
#         return 0
#     else:
#         if x * 2 <= 80:
#             if h % 2 != 0:
#                 return f1(x + 1, h + 1) and f1(x * 2, h + 1)
#             else:
#                 return f1(x + 1, h + 1) or f1(x * 2, h + 1)
#         else:
#             if h % 2 != 0:
#                 return f1(x + 1, h + 1)
#             else:
#                 return f1(x + 1, h + 1)
# for x in range(1, 61):
#     if f(x, 1):
#         print('1', x)
#     if f1(x, 1):
#         print('2', x)
# # 57