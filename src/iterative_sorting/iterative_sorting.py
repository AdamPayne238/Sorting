# TO-DO: Complete the selection_sort() function below ]
# PULLED ARR1 to TEST


arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

"""
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(smallest_index + 1, len(arr)):
            if arr[n] < arr[smallest_index]:
                # TO-DO: swap
                (arr[n], arr[smallest_index]) = (arr[smallest_index], arr[n])
                # Print changed array
                print("selection arr", arr)

    return arr


# TEST IN PAGE
selection_sort(arr)
"""

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # 1. Compare current index and next index
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            current_index = j
            next_index = current_index + 1
            print("curr idx", current_index)
            print("nxt idx", next_index)
            if arr[current_index] > arr[next_index]:
                # 2. If current index is > next index, SWAP
                (arr[current_index], arr[next_index]) = (arr[next_index], arr[current_index])
                print("bubble if arr", arr)
            # 3. Else current index is < next index, PASS
            elif arr[current_index] < arr[next_index]:
                print("bubble else arr", arr)
                pass
                # 4. Move on to next index && Repeat


    return arr


bubble_sort(arr)
print("bubble complete", arr)

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
