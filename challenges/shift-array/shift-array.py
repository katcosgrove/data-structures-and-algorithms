# I asked a friend and he said they used len() after explicitly asking if it was allowed, so this one works. #


def insertShiftArray(arr, val):
    """
Arguments: A list of integers and an integer to be added
Output: A new list with the new value added in the middle
    """
    counter = 0
    new_list = arr + [0]

    for item in arr:
        if counter == len(arr) / 2:
            new_list[counter] = val
            counter += 1

        new_list[counter] = item
        counter += 1
    print(new_list)

insertShiftArray([1, 2, 3, 5, 6, 7], 5)


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
