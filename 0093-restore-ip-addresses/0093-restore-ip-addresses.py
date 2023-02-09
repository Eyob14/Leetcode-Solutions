class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(index, current):
            if len(current) == 4 and index == len(s):
                ans.append(".".join(current[:]))
                return 
 
            for i in range(index, len(s)):
                num = s[index:i + 1]
                if (len(num) > 1 and num[0] == "0") or int(num) > 255:
                    return
                current.append(num)
                dfs(i + 1, current)
                current.pop()
            
            return

        dfs(0, [])

        return ans
        