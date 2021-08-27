#INSERTION SORT
#insert element in correct pos left side is sorted while right is not
def insertion_sort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        j=i-1
        while j>=0 and arr[j]>val:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=val
    return arr
#Time -O(n*n)-but less operations are made best when compaerd with bsort and ssort
#space-O(1)
