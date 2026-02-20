class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        data = set()

        for num in range(len(nums1)):
            if nums1[num] in nums2:
                data.add(nums1[num])

        
        return list(data)


        