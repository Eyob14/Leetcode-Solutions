class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num=0;
        arr = [0]*60

        for t in time:
            k = t%60;

            if k==0:
                num+=arr[k]
            else:
                num+=arr[60-k]

            arr[k] += 1
            
        return num