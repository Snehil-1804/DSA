class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=count2=0
        maj1=maj2=0

        for num in nums:
            if count1==0 and num!=maj2:
                count1=1
                maj1=num
            elif count2==0 and num!=maj1:
                count2=1
                maj2=num
            elif maj1==num:
                count1+=1
            elif maj2==num:
                count2+=1
            else:
                count1-=1
                count2-=1
        res=[]
        threshold=len(nums)//3

        freq1=freq2=0

        for num in nums:
            if maj1==num:
                freq1+=1
            elif maj2==num:
                freq2+=1
        if freq1>threshold:
            res.append(maj1)
        if freq2>threshold:
            res.append(maj2)
        
        return res