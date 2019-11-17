'''
1 <= arr[i] <= n 인 배열중에서 빠진 숫자를 찾는 문제다
공간복잡도를 늘리지 않으면서 o(n)으로 풀어야한다.
input [4,3,2,7,8,2,3,1]
output [5, 6]
'''

class WrongSolution:
    '''
    고민고민하다가 우선 전체 테스트 케이스 통과는 되는지 확인만 해보려고 푼 풀이.
    다른 대상집함을 생성한 다음 원본을 집합으로 변경해서 빼버리고 다시 리스트로 변환했기 때문에 
    공간복잡도를 몹시 사용하는 잘못된 풀이다.
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set([i for i in range(1, len(nums)+1)]) - set(nums))
    

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        value = 0
        ans = []
        for i in range(N):
            '''
            인덱스로 배열의 값을 통해 위치를 찾아서 방문여부를 체크하면, 비어있는 인덱스의 값이 부재한다는 것을 알 수 있다!
            '''
            value = abs(nums[i])-1
            if nums[value] > 0:
                 nums[value] = -nums[value]
        for i in range(N):
            if nums[i] > 0:
                ans.append(i+1)
        return ans