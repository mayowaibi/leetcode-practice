class KthLargest {
    // Heap/Priority Queue Solution
    int k;
    PriorityQueue<Integer> minHeap;

    // TC: O(nlogk), SC: O(k)
    public KthLargest(int k, int[] nums) {
        this.k = k;
        // min-heap with the k largest elements
        this.minHeap = new PriorityQueue<>(k);
        for (int n : nums) {
            this.minHeap.offer(n);
            if (minHeap.size() > k) minHeap.poll();
        }
    }
    
    // TC: O(logk), SC: O(k)
    public int add(int val) {
        minHeap.offer(val);
        if (minHeap.size() > k) minHeap.poll();
        return minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */