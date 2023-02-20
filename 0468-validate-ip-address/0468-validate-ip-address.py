class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in set(list(queryIP)):
            # check if it is IPv4
            ip = queryIP.split(".")
            if len(ip) != 4:
                return "Neither"
            for value in ip:
                if len(value) > 1 and value[0] == '0':
                    return "Neither"
                elif not(1<=len(value)<=3):
                    return "Neither"
                for c in value:
                    if c.isalpha():
                        return "Neither"
                if not(0 <= eval(value) <= 255):
                    return "Neither"

            return "IPv4"
        else:
            # check if it is IPv6
            ip = queryIP.split(":")
            if len(ip) != 8:
                return "Neither"
            for value in ip:
                if not(1 <= len(value)<=4):
                    return "Neither"
                for c in value:
                    if c.isalpha() and not(ord('a') <= ord(c) <= ord('f') or ord('A')<=ord(c)<=ord('F')):
                        return "Neither"
            return "IPv6"
        