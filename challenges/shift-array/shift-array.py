# Doesn't work, but also doesn't use any built-in methods. Progress?
# def insertShiftArray(arr, val):
#     counter = 0
#     new_list = []
#     for item in arr:
#         counter += 1

#     for i in arr:
#         if i > counter // 2:
#             new_list = new_list + arr[i]
#         elif i == counter // 2:
#             new_list = new_list + val
#         else:
#             new_list = new_list + arr[i]
#     print(new_list)

# Doesn't work, and anyway, I don't think slicing lists is allowed
# def insertShiftArray(arr, val):
#     counter = 0
#     new_array = []

#     for item in arr:
#         counter += 1

#     if counter / 2 == 0:
#         counter = counter / 2
#         new_array = arr[0:(counter + 1)] + val
#     else:
#         counter = counter // 2
#         new_array = arr[0:counter] + val

#     print(new_array)
