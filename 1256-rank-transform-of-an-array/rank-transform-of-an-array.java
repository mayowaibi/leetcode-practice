class Solution {
    // Sorting and Hashing Solution - TC: O(nlogn), SC: O(n)
    public int[] arrayRankTransform(int[] arr) {
        HashMap<Integer, Integer> numToRank = new HashMap<>();
        int[] sortedUniqueArr = Arrays.stream(arr).distinct().sorted().toArray();

        for (int i = 1; i <= sortedUniqueArr.length; i++) {
            numToRank.put(sortedUniqueArr[i-1], i);
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i] = numToRank.get(arr[i]);
        }

        return arr;
    }
}