class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        length = len(scores)
        
        age_score = []
        for i, score in enumerate(scores):
            age_score.append((ages[i], score))
        age_score.sort()
        
        dp = [0]*length
        max_score = -1
        
        for i in range(length):
            dp[i] = age_score[i][1]
            for j in range(i-1, -1, -1):
                if age_score[j][1] <= age_score[i][1]:
                    dp[i] = max(dp[i], dp[j] + age_score[i][1])
                    
            max_score = max(dp[i], max_score)
        
        return max_score
                
                
        