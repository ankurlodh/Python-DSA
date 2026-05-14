class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        mapping = {}

        for num in nums2:

            while stack and num > stack[-1]:
                mapping[stack.pop()] = num

            stack.append(num)

        result = []

        for num in nums1:
            result.append(mapping.get(num, -1))

        return result