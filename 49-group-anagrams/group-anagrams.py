class Solution:
    # Optimal Hashmap Solution
    # TC: O(m*n*26) = O(m*n) where m = num of strs and n = avg len of each str
    # SC: O(26) = O(1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map char count of each str to list of anagrams
        anagram_map = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # change count (key) to tuple because lists cannot be keys
            anagram_map[tuple(count)].append(s)
        
        return list(anagram_map.values())

    # Sorting + Hashmap Solution
    # TC: O(m*nlogn) where m = num of strs and n = avg len of each str
    # SC: O(n)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)

        for s in strs:
            # use sorted version of each string as key for map
            sorted_str = ''.join(sorted(s))
            anagram_map[sorted_str].append(s)
        
        return list(anagram_map.values())
