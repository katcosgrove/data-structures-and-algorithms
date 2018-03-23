def LargestArray(arr):
    
"""
Finds the largest product in a 2D array
"""
    answer = 0
    counter = 0
    new_arr = []

    for item in arr:
        new_arr[counter] = item[0] * item[1]
        counter += 1
    for item in new_arr:
        if item > answer:
            answer = item
    return answer

