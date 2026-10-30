class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "$" + s + ","

        return string

    def decode(self, s: str) -> List[str]:
        strs = []

        print(s)
        i = 0
        while i < len(s):
            if s[i] == "$":
                length = ""
                j = i - 1
                while s[j].isdecimal() and j >= 0:
                    length += s[j]
                    j = j - 1

                length = int(length[::-1])
                strs.append(s[i + 1:i + length + 1])
                i = i + length

            i = i + 1

        return strs