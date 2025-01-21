def quicksort(arr):
    # check for the size of the array, if less than 1 element, then  nothing needs to be done
    if len(arr) <= 1:
        return arr

    # Choosing the pivot as the last element of the array
    pivot = arr[-1]

    # Initializing the left array and putting all elements less than the pivot in the array
    left = []
    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
    
    # Creating the right array with all elements greater than or equal to the pivot
    right = []
    for i in arr[:-1]:
        if i >= pivot:
            right.append(i)

    # call recursive function to sort left and right, and combine the arrays
    return quicksort(left) + [pivot] + quicksort(right)

