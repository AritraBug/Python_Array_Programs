# Program to reverse the elements of an array

def reverse_array(arr):
    # Initialize two pointers: one at the start, the other at the end of the array
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap elements at the start and end pointers
        arr[start], arr[end] = arr[end], arr[start]
        # Move pointers towards the center
        start += 1
        end -= 1
    return arr

# Example array
arr = [1, 2, 3, 4, 5]
print("Reversed array:", reverse_array(arr))

# contributed by AritraBug