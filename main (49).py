def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        while j >=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,6,7,8,9,3]
insertion_sort=arr
print(insertion_sort)