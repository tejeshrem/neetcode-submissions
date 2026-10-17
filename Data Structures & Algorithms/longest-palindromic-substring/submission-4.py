class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        res = s[0]
        maxLength = len(res)

        for i in range(len(s)):

            l,r = i-1, i+1
            substring = ""
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxLength:
                    res = s[l:r+1]
                    maxLength = r-l+1
                l-=1
                r+=1
                     
            l,r = i, i+1  


            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxLength:
                    res = s[l:r+1]
                    maxLength = r-l+1
                l-=1
                r+=1
            


        return res              
                

        