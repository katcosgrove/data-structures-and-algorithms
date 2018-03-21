# I asked a friend and he said they used len() after explicitly asking if it was allowed, so this one works. #


# def insertShiftArray(arr, val):
#     """
# Arguments: A list of integers and an integer to be added
# Output: A new list with the new value added in the middle
# Issues: Working on making this one account fo ran odd array
#     """
#     counter = 0
#     odd = counter + 1
#     new_list = arr + [0]

#     for item in arr:
#         if counter == len(arr) / 2:
#             new_list[counter] = val
#             counter += 1
#         else:
#             counter += 1
#             new_list[odd] = val
#             new_list[counter] = item

#     print(new_list)

# insertShiftArray([1, 2, 3, 4, 5, 6, 7], 5)


def insertShiftArray(arr, val):
    """
Arguments: A list of integers and an integer to be added
Output: A new list with the new value added in the middle
Issues: This one accounts for an even array, but not odd
    """
    counter = 0
    new_list = arr + [0]

    for item in arr:
        if counter == len(arr) / 2:
            new_list[counter] = val
            counter += 1

        new_list[counter] = item
        counter += 1

    return(new_list)

insertShiftArray([20, 30, 59, 70], 200)


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
