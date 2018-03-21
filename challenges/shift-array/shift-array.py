
# Doesn't work, but also doesn't use any built-in methods. Progress?
# def insertShiftArray(arr, val):
#     counter = 0
#     new_list = []
#     for item in arr:
#         counter += 1

#     counter = counter // 2

#     for i in arr:
#         if arr[i] > counter:
#             new_list[i] = new_list + arr[i]
#         elif arr[i] == counter:
#             new_list[i] = new_list + val
#         else:
#             new_list[i] = new_list + arr[i]
#     print(new_list)

# insertShiftArray([1, 2, 3, 4], 5)


# Also doesn't work, and anyway, I don't think slicing lists is allowed
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
