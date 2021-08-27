#SELECTION SORT
#THINK LIKE A PILE OF CARDS AND MOVING SMALLEST CARD TO OTHER SIDE
def selection_sort(arr):
    for i in range(len(arr)):
        miny=i
        for j in range(i+1,len(arr)):  #finding smallest number
            if arr[miny]>arr[j]:
                miny=j                 #swap
        #swap
        arr[miny],arr[i]=arr[i],arr[miny]
    return arr
#Time -O(n*n)
#space-O(1)
