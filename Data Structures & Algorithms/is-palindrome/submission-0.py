class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=s.lower()
        l=0
        r=len(result)-1
        while l<r:
            if not result[l].isalnum():
                l=l+1
                continue
            if not result[r].isalnum():
                r=r-1
                continue
            if result[l]!=result[r]:
                return False
            l=l+1
            r=r-1
        return True
