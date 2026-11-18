class Solution:
    def solve(self,index,total,bracket,result):
        if index>=len(bracket):
            if total==0:
                result.append(".".join(bracket))
            return
        if total>len(bracket)//2:
            return
        elif total<0:
            return
        bracket[index]="("
        sum=total+1
        self.solve(index+1,sum,bracket,result)
        bracket[index]=")"
        sum=total-1
        self.solve(index+1,total,bracket,result)
        return result

    def generateParenthesis(self, n: int) -> list[str]:
        bracket=[""]*(n*2)
        result=[]
        self.solve(0,0,bracket,result)

        