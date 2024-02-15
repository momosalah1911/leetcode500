class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def myFunc(e):
            return e[1]
        l=list(enumerate(nums))
        l.sort(key=myFunc)
        i,j=0,len(l)-1
        # print(nums[i])
        for k in range(len(nums)-1): 
            if l[i][1]+l[j][1]==target:
                return [l[i][0],l[j][0]]
            elif l[i][1]+l[j][1]>target:
                j=j-1
            else:
                i=i+1

           
            

