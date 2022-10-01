"""
Binary search
The fastest search algorithm with (Ologn) time complexity
"""
from typing import List

class Solution:
    def search(self,nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1 #remember to put right or end as len(nums)-1 not len(nums)
        result=None
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]>target:# if mid is greater than target
                right=mid-1 #decrease the right bound
            elif nums[mid]<target:
                left=mid+1
            else:
                result=mid
                right=mid-1 # Decrease the right bound to find the first occurence
        if result==None:
            return -1
        return result


def main():
    soln=Solution()
    array,target=[10,6,4],10
    search_index=soln.search(array,target)
    print("The element was found at index",search_index)

main()


