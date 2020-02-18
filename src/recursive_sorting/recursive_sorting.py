# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move toward the base case.
# 3. A recursive algorithm must call itself, recursively.

# EXAMPLE Print every number, start at number, until you reach 0
# def recurse(number):
#   if number <= 0:  # Base case
#       return # if number is less than or equal to 0, return ends the recursion
#   print(number) # print the number
#   number -= 1 # decrement number by 1
#   recurse(number) #recurse number

# recurse(5) # Recursion calls itself, recursively

# arrA = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arrB = [0, 1, 2, 3, 4, 5, 8, 3]


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    arrA.extend(arrB)
    for index in range(len(merged_arr)):
        merged_arr[index] = arrA[index]
    print(merged_arr)
    return merged_arr


# merge(arrA, arrB)


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
