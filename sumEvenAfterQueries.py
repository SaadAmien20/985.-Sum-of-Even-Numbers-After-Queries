class soulation(object):
    def __init__(self,nums,queries):
        self.nums = nums 
        self.queries = queries

    def sum_after_queries(self):
        """
        type:nums: list[int]
        type:queries:list[list[int]]
        rtype:list[int ]
        """
        answer = []
        sum_element = 0
        for q in queries:
            nums[q[1]] += q[0]
            for i in nums:
                if i %2==0:
                    sum_element += i
            answer.append(sum_element)
            sum_element=0
        return answer 

nums = [1,2,3,4]  
queries = [[1,0],[-3,1],[-4,0],[2,3]]

s1 = soulation(nums,queries)
print (s1.sum_after_queries())