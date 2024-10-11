class Solution {
    // Sorting Solution - TC: O(m*nlogn), SC: O(m)
    public List<List<String>> groupAnagrams(String[] strs) {
        // Map the sorted version of each word in strs (key) to its anagrams (value)
        Map<String, List<String>> anagramMap = new HashMap<>(); // SC: O(m)

        // TC: O(m), m is the number of strings in strs
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars); // TC: O(nlogn), n is the avg word length of each string
            String sortedStr = new String(chars);

            if (!anagramMap.containsKey(sortedStr)) {
                anagramMap.put(sortedStr, new ArrayList<>());
            }
            anagramMap.get(sortedStr).add(str);
        }

        return new ArrayList<>(anagramMap.values());
    }
}