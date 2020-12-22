class MaxHeap:
    def buildHeap(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.maxHeapify(arr,i,n)

        return arr

    def maxHeapify(self,arr,index,n):
        leftChild = 2 * index
        rightChild = (2*index)+1
        largestIndex = n-1
        if leftChild < n and arr[leftChild]> arr[largestIndex]:
            largestIndex = leftChild
        elif rightChild < n and arr[rightChild]> arr[largestIndex]:
            largestIndex = rightChild

        if largestIndex != index:
            temp = arr[index]
            arr[index] = arr[largestIndex]
            arr[largestIndex] = temp
            self.maxHeapify(arr,largestIndex,n)

heap = MaxHeap()
arr = [2,10,7,8,4,9]
print(heap.buildHeap(arr))
