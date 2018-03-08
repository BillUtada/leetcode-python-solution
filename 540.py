class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1;
        r = len(nums);
        while True:
            if l == r:
                return nums[l-1];
            mid = (l+r)/2;
            if nums[mid-1] == nums[mid-2]:
                if (mid-l-1)%2 == 0:
                    l = mid + 1;
                    continue;
                else:
                    r = mid - 2;
                    continue;
            elif nums[mid-1] == nums[mid]:
                if (mid-l)%2 == 0:
                    l = mid + 2;
                    continue;
                else:
                    r = mid - 1;
            else:
                return nums[mid-1];
                
            
