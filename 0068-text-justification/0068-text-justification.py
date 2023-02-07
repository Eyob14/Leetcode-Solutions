class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        temp = [words[0]]
        count = len(words[0])
        
        for i in range(1, len(words)):
            if count + len(words[i]) >= maxWidth:
                j = 1
                if ' ' in temp:
                    while count < maxWidth:
                        if ' ' in temp[j]:
                            temp[j] += ' '
                            count += 1
                        j += 1
                        if j == len(temp):
                            j = 0
                else:
                    temp.append(' '*(maxWidth-count))
                    
                answer.append(''.join(temp))
                temp = [words[i]]
                count = len(words[i])
            else:
                temp.append(' ')
                temp.append(words[i])
                count += 1 + len(words[i])

        temp = ''.join(temp)
        temp += ' ' * (maxWidth-count)
        answer.append(temp)

        return answer
                    
            