class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        for i in range(len(s)):
            if s[i].isalnum():
                
                while not s[j].isalnum():
                    j -= 1
                
                if s[i].lower() != s[j].lower():
                    print(f"{i} {s[i]} {s[j]}")
                    return False
                
                j -= 1
        
        return True