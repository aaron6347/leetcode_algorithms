"""#167_two_sum_2-input_array_is_sorted.py
    Created by Aaron at 30-Apr-20"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # app1
        # dic={}
        # for x in range(len(numbers)):
        #     find=target-numbers[x]
        #     if find in dic:
        #         return [dic[find]+1, x+1]
        #     dic[numbers[x]]=x

        # app2
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

run=Solution()
a,b=[2,7,11,15],9
print(run.twoSum(a,b))
# app1 using dictionary to find pair for the sum
# app2 using 2 pointer left and right, sum of both to determine movement of pointers