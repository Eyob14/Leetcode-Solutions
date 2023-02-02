class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log = []
        letter_log = []

        for logFile in logs:
            file = logFile.split()
            if file[1].isdigit():
                digit_log.append(logFile)
            else:
                letter_log.append(file)
        letter_log.sort(key=lambda log: (log[1:],log[0]))
        letter_log = [" ".join(log) for log in letter_log]
        return letter_log+digit_log