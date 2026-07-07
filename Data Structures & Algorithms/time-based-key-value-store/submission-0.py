class TimeMap:
    """
    Time-based key-value store using hash map and binary search.
    
    Time Complexity:
    - set: O(1) - append to list
    - get: O(log n) - binary search on timestamps, n = number of timestamps for key
    
    Space Complexity: O(m * n) where m = unique keys, n = average timestamps per key
    """

    def __init__(self):
        """Initialize the data structure."""
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store key-value pair with timestamp.
        
        Args:
            key: The key to store
            value: The value to store
            timestamp: The timestamp (strictly increasing for each key)
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        Get value at timestamp (or closest earlier timestamp).
        
        Args:
            key: The key to look up
            timestamp: The query timestamp
            
        Returns:
            Value with largest timestamp <= query timestamp, or "" if none exists
        """
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        
        while (left <= right):
            mid = left + (right - left) // 2
            
            t, v = values[mid]
            if t == timestamp:
                return v
            
            if t > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                
        return values[left - 1][1] if values[left - 1][0] < timestamp else ""
