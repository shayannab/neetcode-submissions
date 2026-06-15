class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        l, r = 0, len(pairs) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]  # valid, but maybe larger ts exists
                l = mid + 1             # try right for larger timestamp
            else:
                r = mid - 1             # too large, go left

        return result