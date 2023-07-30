class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> letters1 = new HashMap<>(); // letter : no. of occurences
        for (int i = 0; i < s.length(); i++) {
            if (letters1.containsKey(s.charAt(i))){
                letters1.put(s.charAt(i), letters1.get(s.charAt(i))+1);
            } else {
                letters1.put(s.charAt(i), 1);
            }
        }
        Map<Character, Integer> letters2 = new HashMap<>(); // letter : no. of occurences
        for (int i = 0; i < t.length(); i++) {
            if (letters2.containsKey(t.charAt(i))){
                letters2.put(t.charAt(i), letters2.get(t.charAt(i))+1);
            } else {
                letters2.put(t.charAt(i), 1);
            }
        }
        return letters1.equals(letters2);
    }
}