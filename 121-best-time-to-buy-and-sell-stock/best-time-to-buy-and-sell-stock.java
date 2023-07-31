class Solution { // Sliding Window
    public int maxProfit(int[] prices) {
        int left = 0; // But
        int right = 1; // Sell
        int maxProfit = 0;
        while (right < prices.length) {
                int currentProfit = prices[right] - prices[left];
                if (prices[left] < prices[right]) {
                    maxProfit = Math.max(currentProfit, maxProfit);
                }
                else {
                    left = right;
                }
                right += 1;
        }
        return maxProfit;
    }
}