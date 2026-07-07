class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        dict_s = {}
        for ch in t:
            dict_t[ch] = 1 + dict_t.get(ch, 0)

        required = len(dict_t)
        matched = 0
        min_len = float("infinity")
        best_indexes = [-1, -1]
        left = 0
        
        for right in range(len(s)):
            ch = s[right]
            dict_s[ch] = 1 + dict_s.get(ch, 0)
            
            if ch in dict_t and dict_s[ch] == dict_t[ch]:
                matched += 1
                
            while matched == required:
                if right - left + 1 < min_len:
                    best_indexes = [left, right] # Found better!
                    min_len = right - left + 1
                    
                left_char = s[left]
                if left_char in dict_t and dict_s[left_char] == dict_t[left_char]:
                    matched -= 1
                    
                dict_s[s[left]] -= 1
                left += 1
            
        return (
            ""
            if min_len == float("infinity")
            else s[best_indexes[0] : best_indexes[1] + 1]
        )
        