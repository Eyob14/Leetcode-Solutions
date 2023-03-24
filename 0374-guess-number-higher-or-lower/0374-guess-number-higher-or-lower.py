# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        md=n//2
        l=0
        r=n
        x=guess(md)
        while(x!=0 and l<r):
            print(md)
            if(x==1):
                l=md+1
                md=(l+r)//2
                x=guess(md)
            else:
                r=md-1
                md=(l+r)//2
                x=guess(md)
        return md