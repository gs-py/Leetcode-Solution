class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast=1
        slow=0
        k=0
        if len(nums)==1:
            return 1
            

        
        while(fast<len(nums)):           
            while(nums[slow] == nums[fast]):
                if fast<len(nums)-1:
                    fast += 1
                else:
                    nums[k]=nums[slow]
                    fast=fast+1
                    break
           
            if((fast-slow)== 1):
                nums[k]=nums[slow]               
                k=k+1 
                slow=fast                
            elif((fast-slow) == 2):               
                nums[k]=nums[slow]
                nums[k+1]=nums[slow]
                k=k+2
                slow=fast 
               
            elif((fast-slow)>2):
                nums[k]=nums[slow]
                nums[k+1]=nums[slow]
                k=k+2
                slow=fast                
        
          
        
        return k
