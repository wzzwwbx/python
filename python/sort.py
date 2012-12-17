
import sys
import random

#MAX_NUM = sys.maxint*2+1
MAX_NUM = 100*2+1

def getRandom():
    return random.randrange(0, MAX_NUM)

def getRandomList(sortNum):
    arr=[]
    for i in range(sortNum):
        arr.append(getRandom())
    return arr

#insert sort
def insertSort(arr):
    for i in range(len(arr)-1):
        key = arr[i+1]
        j = i
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

#quick sort
def quickSort(arr, start, end):
    if(start >= end):
        return
    left = start - 1
    right = start
    while(right <= end):
        if(arr[right]<arr[end] or right==end):
            left += 1
            arr[left], arr[right] = arr[right], arr[left]
        right += 1
    quickSort(arr, start, left-1)
    quickSort(arr, left+1, end)

#merge sort
def mergeSort(arr):
    def merge(arr, temp, i, m, n):
        k = i
        j = m + 1
        while(i <= m and j <= n):
            if(arr[i] <= arr[j]):
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        while(i <= m):
            temp[k] = arr[i]
            k += 1
            i += 1
        while(j <= n):
            temp[k] = arr[j]
            k += 1
            j += 1
    
    def mergePass(arr, temp, length):
        i = 0
        while(i+2*length < len(arr)):
            merge(arr, temp, i, i+length-1, i+2*length-1)
            i += 2 * length
        if(i+length < len(arr)):
            merge(arr, temp, i, i+length-1, len(arr)-1)
        else:
            j = i
            while(j < len(arr)):
                temp[j] = arr[j]
                j += 1
    
    temp = [0 for x in range(len(arr))]
    leng = 1
    while(leng < len(arr)):
        mergePass(arr, temp, leng)
        leng *= 2
        mergePass(temp, arr, leng)
        leng *= 2
 

#heap sort
def heapSort(arr):
    def heapify(arr):
        start = (len(arr) - 2) / 2
        while(start >= 0):
            siftDown(arr, start, len(arr)-1)
            start -= 1
                
    def siftDown(arr, start, end):
        root = start
        while(root*2+1 <= end):
            child = root * 2 + 1
            if(child+1 <= end and arr[child] < arr[child+1]):
                child += 1
            if(child <= end and arr[root] < arr[child]):
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return
    
    heapify(arr)
    end = len(arr) - 1
    while(end > 0):
        arr[end], arr[0] = arr[0], arr[end]
        siftDown(arr, 0, end-1)
        end -= 1
            
if __name__ == '__main__':
    sslist = getRandomList(40)
    print sslist
#    insertSort(sslist)
#    quickSort(sslist, 0, len(sslist)-1)
#    mergeSort(sslist)
    heapSort(sslist)
    print sslist
