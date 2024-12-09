"""
3152. Special Array II
Medium
Topics
Companies
Hint
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""
nums1 = [3,4,1,2,6]
queries1 = [[0,4]]
nums2 = [4,3,1,6]
queries2 = [[0,2],[2,3]]

class My_solution:
    def isArraySpecial(self, nums, queries):
        def even_or_odd(n):
            if n % 2 == 0:
                return 2
            else:
                return 1
        answers = []

        for i in range(len(queries)):
            frm = queries[i][0]
            to = queries[i][1]
            parity = True

            for j in range(frm, to):
                if even_or_odd(nums[j]) == even_or_odd(nums[j + 1]):
                    parity = False
                    break
            answers.append(parity)
        return answers
# sol = My_solution()
# print(sol.isArraySpecial(nums1, queries1))  #[False]
# print(sol.isArraySpecial(nums2, queries2))  #[False, True]
#❌❌TIME LIMIT EXCEEDED❌❌    

#from solutions😭
class Solution:
    def isArraySpecial(self, nums, queries):
        l = 0
        previous = nums[0]
        p = []
        for i in range(1, len(nums)):
            if (nums[i]+previous) % 2 == 0:
                p.append([l,i-1])
                l = i
            previous = nums[i]
        p.append([l,len(nums)-1])
        res = []
        for q in queries:
            l, r = 0, len(p)-1
            i = 0
            while l<=r:
                m = (l+r+1)//2
                if q[0] >= p[m][0]:
                    i = m
                    l = m+1
                else:
                    r = m-1
            if q[1] <= p[i][1]:
                res.append(True)
            else:
                res.append(False)
        return res

#this is from larry (pro algorithmist🔥)

class Larry_solution:
    def isArraySpecial(self, nums, queries):
        N = len(nums)
        
        breaks = []

        for i in range(N - 1):
            if nums[i] % 2 == nums[i - 1] % 2:
                breaks.append(i)
        
        ans = []
        for start, end in queries:
            left = bisect.bisect_left(breaks, start)
            right = bisect.bisect_left(breaks, end)

            #print(left, right)
            ans.append(left == right)
        return ans

#leetcode's editorial solution
#1. binary search approach
class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[Tuple[int, int]]
    ) -> List[bool]:
        ans = [False] * len(queries)
        violating_indices = []

        for i in range(1, len(nums)):
            # same parity, found violating index
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            found_violating_index = self.binarySearch(
                start + 1, end, violating_indices
            )

            if found_violating_index:
                ans[i] = False
            else:
                ans[i] = True

        return ans

    def binarySearch(
        self, start: int, end: int, violating_indices: List[int]
    ) -> bool:
        left = 0
        right = len(violating_indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            violating_index = violating_indices[mid]

            if violating_index < start:
                # check right half
                left = mid + 1
            elif violating_index > end:
                # check left half
                right = mid - 1
            else:
                # violatingIndex falls in between start and end
                return True

        return False

#2. prefix sum approach
class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                # new violative index found
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            ans[i] = prefix[end] - prefix[start] == 0

        return ans

#3. sliding window approach
class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        n = len(nums)
        max_reach = [0] * n
        end = 0

        # Step 1: Compute the maximum reachable index for each starting index
        for start in range(n):
            # Ensure 'end' always starts from the current index or beyond
            end = max(end, start)
            # Expand 'end' as long as adjacent elements have different parity
            while end < n - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            # Store the farthest index reachable from 'start'
            max_reach[start] = end

        ans = []

        # Step 2: Answer each query based on precomputed 'max_reach'
        for start, end_query in queries:
            # Check if the query range [start, end] lies within the max reachable range
            ans.append(end_query <= max_reach[start])
        return ans
