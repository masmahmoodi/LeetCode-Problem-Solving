class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        for i in range(len(nums)):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count +=1

            if count > len(nums) //2 :
                return nums[i]
            
        

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count =0
        condidate = None
        for num in nums:
            if count == 0:
                condidate = num
            if condidate == num:
                count +=1
            else:
                 count -=1
        return  condidate 