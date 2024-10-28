# Check if given array is Monotonic
"""An array is monotonic if it is either monotone increasing or monoto
ne decreasing. An array A is monotone increasing if 
for all i <= j, A[i] <= A[j]. """
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))
