#binary search 
#Returns the index of x in arr if present
def binary_search(arr, low,high, x):
    if high >= low:
        mid = (high + low) // 2
        #if in middle
        if arr[mid] == x:
            return mid
        #if smaller than mid -> in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        #else the element can only be in right subarray
        else:
            return binary_search(arr, mid+1, high, x)
    #element is not in array
    else:
        return -1

arr = [3,4,10,40,2]
x = 10

#callig function
result = binary_search(arr,0,len(arr)-1,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
        
            













