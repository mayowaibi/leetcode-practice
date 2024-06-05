class Solution:
    # Hashmap (Counter) Solution - TC: O(n), SC: O(n)
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        # Create a char counter hashmap for the first word
        hashmap = Counter(words[0])
        
        # For every other word in words, get the min no. of
        # occurences for each char in the first word
        for i in range(1, len(words)):
            for key in hashmap:
                hashmap[key] = min(words[i].count(key), hashmap[key])

        # If the no. of occurences is 0, then the char does
        # not appear in at least one of the words
        for key in hashmap:
            if hashmap[key] != 0:
                # Loop to ensure char is added to result multiple times if needed
                for i in range(hashmap[key]):
                    result.append(key)
        
        return result