class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        left =0
        right =n-1
        while left <=right:
            mid = (left +right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[left]:
                if target<=nums[mid] and target>=nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target>=nums[mid] and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
                  
                
        