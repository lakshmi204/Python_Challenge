# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print(1//2)
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                t1=mid
                valleft=t1
                while valleft>left and nums[valleft-1]==target:
                    val1=valleft-1
                    valleft-=1
                valri=t1
                while valri<right and nums[valri+1]==target:
                    val2=valri+1
                    valri+=1
                return [valleft,valri]
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]
