class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtracking(start_index, path):
            if start_index == len(digits):
                result.append(path)
                return
            
            cur_letters = phone[digits[start_index]]
            for ele in cur_letters:
                backtracking(start_index+1, path+ele)
        backtracking(0, "")
        return result