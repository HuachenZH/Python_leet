class Solution:
    def digitSum(self,n:int) -> int:
        '''Get all the digits of a number and sum them up.'''
        table=[]
        # get the one digit
        table.append(n%10)
        # get the other digits
        for i in range(len(str(n))-1):
            n=(n-table[len(table)-1])/10
            table.append(int(n%10))
        res=0
        for i in table:
            res+=i
        return res
    
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # create the balls list
        ballList=[]
        ballList.append([i for i in range(lowLimit,highLimit+1)])
        ballList=ballList[0]
        # create the box dictionary
        ballsInBox={}
        for ball in ballList:
            digiSum=self.digitSum(ball)
            ballsInBox[digiSum]=ballsInBox.get(digiSum,0)+1
        # find which key contains greatest value
        # in fact this is not what we are looking for
        maxKey=[key for key,value in ballsInBox.items() if value==max(ballsInBox.values())][0]
        return max(ballsInBox.values())
