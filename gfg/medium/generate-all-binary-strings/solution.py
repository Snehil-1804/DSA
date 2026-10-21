class Solution:
    
    def solve(self,index,number,result):
        if index>=len(number):
            result.append("".join(number))
            return 
        number[index]="0"
        self.solve(index+1,number,result)
        
        number[index]="1"
        self.solve(index+1,number,result)
    def binstr(self, n):
        # code here
        numbers = ["0"] * n
        result = []
        self.solve(0, numbers, result)
        return result
        