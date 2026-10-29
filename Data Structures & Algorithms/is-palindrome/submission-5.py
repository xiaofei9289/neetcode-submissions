class Solution:
    def isPalindrome(self, s: str) -> bool:
        deal_ed_s = ""
        for ele in s:
            if ele.isalnum():
                deal_ed_s += ele.lower()
        
        lef = 0 
        rig = len(deal_ed_s)-1

        while lef <= rig:
            if deal_ed_s[lef] == deal_ed_s[rig]:
                lef += 1
                rig -= 1
            else:
                return False
        return True