# Boyer-Moore Voting Algorithm

# Intuition

# If we had some way of counting instances of the majority element as +1
# and instances of any other element as −1, summing them would make it
# obvious that the majority element is indeed the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityElement = None
        
        for num in nums:
            if count == 0:
                majorityElement = num
            
            count += 1 if num == majorityElement else -1
        
        return majorityElement