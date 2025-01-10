class Solution:
    # Double Hashmap Solution - TC: O(n+m)*, SC: O(1) assuming output arr doesn't count
    # *n and m are the total number of chars in words1 and words2 respectively
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Use hashmap to store the max frequency of
        # every char that appears in the words in words2
        max_freq = {}   # SC: O(26)
        for word in words2:
            for char, freq in Counter(word).items():
                if char not in max_freq or max_freq[char] < freq:
                    max_freq[char] = freq
        
        res = []

        # Create a Counter for every word in words1,
        # then check that each char count is >= to the
        # char count in max_freq before it can be added to res
        for word in words1:
            universal = True
            char_count = Counter(word)  # SC: O(26)
            for char, freq in max_freq.items():
                if char not in char_count or char_count[char] < freq:
                    universal = False
                    break
            if universal:
                res.append(word)

        return res