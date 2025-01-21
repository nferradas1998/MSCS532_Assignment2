def mergesort(arr):
    # check for the size of the array, if less than 1 element, then  nothing needs to be done
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Get the middle element
    left = mergesort(arr[:mid])  # call recursive method to sort left side
    right = mergesort(arr[mid:])  # call recursive method to sort right side

    # sort and merge the two halves
    return sort(left, right)

def sort(left, right):
    sorted = []  # Initialize the array to be returned
    l = 0 # Initialize pointer for left array
    r = 0 # Initialize pointer for right array

    # Compare elements and insert them to sorted array
    while l < len(left) and r < len(right):
        if left[l] < right[r]:  # if element from the left is smaller than element from the right, appened element from left array
            sorted.append(left[l])
            l += 1
        else: # element from the rigth is smaller, append it to the sorted array
            sorted.append(right[r])
            r += 1

    # if any elements are left in any of left or right arrays, add them to sorted array
    sorted.extend(left[l:])
    sorted.extend(right[r:])

    return sorted

