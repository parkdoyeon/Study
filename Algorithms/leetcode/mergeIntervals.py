class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        ans = [intervals.pop(0)]
        for item in intervals:
            last = ans.pop(len(ans)-1)
            if last[1] >= item[0]:
                if last[1] > item[1]:
                    last = [last[0], last[1]]
                else:
                    last = [last[0], item[1]]
                ans.append(last)
            else:
                ans.append(last)
                ans.append(item)
        return ans