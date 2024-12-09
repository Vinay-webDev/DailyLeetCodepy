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
sol = My_solution()
print(sol.isArraySpecial(nums1, queries1))  #[False]
print(sol.isArraySpecial(nums2, queries2))  #[False, True]
#❌❌TIME LIMIT EXCEEDED❌❌    


