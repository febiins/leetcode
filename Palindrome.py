class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for ch in s:
            if ch.isalnum():
                strs+=ch.lower()
        return strs==strs[::-1]        
        
