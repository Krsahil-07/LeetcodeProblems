class Solution {
    public int smallestIndex(int[] nums) {
        int ans=-1;
        for(int i=0;i<nums.length;i++){
            if (solve(nums[i])==i){
                ans=i;
                break;
            }
        }
        return ans;
        
    }
    private int solve(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
