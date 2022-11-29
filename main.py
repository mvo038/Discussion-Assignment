# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")
# must be in-place sort
def merge_sort(arr,cmp):
    
if len(arr) > 1:
 
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)
 
    i = 0
    j = 0
    k = 0
        # Copy data to temp arrays L[] and R[]
    while cmp(i, len(L)) < 0 and cmp(j, len(R)) < 0:
        if cmp(L[i], R[j]) < 0:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
        # Checking if any element was left
    while cmp(i, len(L)) < 0:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while cmp(j, len(R)) < 0:
        arr[k] = R[j]
        j += 1
        k += 1
# must be in-place sort
def quick_sort(arr,cmp):
    pass
