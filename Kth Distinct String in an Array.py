
class Solution:
   
    from collections import Counter
    def kthDistinct(self, arr: List[str], k: int) -> str:
        

        n= Counter(arr)

        names=[name for name,count in n.items() if count ==1]

        if k <= len(names):
            return names[k-1]
        else:
            return ""
            


        
