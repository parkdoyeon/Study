class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        #self.quickSortTwo(nums)
        return nums
    
    def quickSort(self, arr, left: int, right: int) -> List[int]:
        if left >= right:
            return
        pivot = self.partition(arr, left, right)
        self.quickSort(arr, left, pivot-1)
        self.quickSort(arr, pivot, right)
    
    def partition(self, arr, left, right):
        # 내가 제일 삽질한 부분
        # pivot값이 위치가 변경되라도 한번의 루프에서는 left, right가 교차하기 전까지는 pivot기준으로 비교를 해줘야한다!
        pivot = arr[(left+right)//2]

        while left <= right:
             # 나는 요기서 pivot의 실제 값이 아닌 index값으로
             # arr[pivotidx]비교를 해서 일부가 정렬이 되지 않았었다.
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            #print(left, pivot, right, arr)
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right -1
        return left
    
    # 내부 함수 구조로 구현
    # 함수 파라미터 구간에서 메모리 누수를 막고자한 것 같은데 실제로는 1mb메모리를 더 사용한다..
    # 실제로 속도도 느리고 음??
    def quickSortTwo(self, arr):
        def sort(low, high):
            if high <= low:
                return

            mid = partition(low, high)
            sort(low, mid - 1)
            sort(mid, high)

        def partition(low, high):
            pivot = arr[(low + high) // 2]
            while low <= high:
                while arr[low] < pivot:
                    low += 1
                while arr[high] > pivot:
                    high -= 1
                if low <= high:
                    arr[low], arr[high] = arr[high], arr[low]
                    low, high = low + 1, high - 1
            return low
        return sort(0, len(arr) - 1)

sol = Solution()
print(sol.sortArray([-1,2,-8,-10]))