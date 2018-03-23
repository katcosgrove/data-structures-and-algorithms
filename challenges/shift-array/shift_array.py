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

# def insertShiftArray(arr, val):
#     """
# Arguments: A list of integers and an integer to be added
# Output: A new list with the new value added in the middle
# Issues: This one accounts for an even array, but not odd
#     """
#     counter = 0
#     new_list = arr + [0]

#     for item in arr:
#         if counter == len(arr) / 2:
#             new_list[counter] = val
#             counter += 1

#         new_list[counter] = item
#         counter += 1

#     return(new_list)

# insertShiftArray([20, 30, 59, 70], 200)


# This works now, if it's okay to use range()
def insertShiftArray(arr, num):
    answer = [0] * (len(arr) + 1)
    middle = (len(arr) + len(arr) % 2) // 2

    for item in range(len(answer)):
        if item < middle:
            answer[item] = arr[item]
        elif item == middle:
            answer[item] = num
        else:
            answer[item] = arr[item - 1]
    return answer
