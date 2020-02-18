# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
           if arr[j] < arr[smallest_index]:
               smallest_index = j
        
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
             
    return arr


        # TO-DO: swap

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
# loop through length of array - 1
# get first item in the array 
# compare first element to the next
# if first element is greater than the next, swap 
    for i in range (0, len(arr) - 1):
        # cur_index = i
        # next_index = cur_index + 1
        for j in range(i +1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr