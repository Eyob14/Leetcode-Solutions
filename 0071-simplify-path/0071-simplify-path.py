class Solution:
    def simplifyPath(self, path: str) -> str:
        answer = []
        paths = path.split("/")
        for path in paths:
            if answer and path == "..":
                answer.pop()
            elif path not in {".", "", ".."}:
                answer.append(path)
                
        return "/"+"/".join(answer)