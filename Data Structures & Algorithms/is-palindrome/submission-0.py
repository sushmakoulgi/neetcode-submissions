class Solution:
    def isPalindrome(self, s: str) -> bool:
        input=[]
        for char in s:
            if char.isalnum():
                input.append(char.lower())

        print(input)
        return input[::1]==input[::-1]