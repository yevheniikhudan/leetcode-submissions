class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delimiter = '#'
        
        for s in strs:
            encoded = encoded + str(len(s)) + delimiter + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        delimiter = '#'
        end = 0
        pointer = 0

        while pointer < len(s):
            while (s[pointer] != delimiter):
                pointer += 1
            start = pointer + 1
            nextLength = int(s[end:pointer])
            end = start + nextLength
            decoded.append(s[start:end])
            pointer = end

        return decoded
        
