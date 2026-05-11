class Solution:
    def getSecondLargest(self, arr):
        largest = secondlargest = -1

        for num in arr:
            if num > largest:
                secondlargest = largest
                largest = num
            elif num > secondlargest and num != largest:
                secondlargest = num

        return secondlargest