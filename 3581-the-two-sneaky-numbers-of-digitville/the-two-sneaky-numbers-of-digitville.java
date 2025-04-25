class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        HashMap<Integer,Integer> dt = new HashMap<>();
        for(int val: nums){
            dt.put(val,dt.getOrDefault(val,0)+1);
        }
        int ans[]=new int[2];
        int n=0;
        for(int k:dt.keySet()){
            if(dt.get(k)==2){
                ans[n]=k;
                n++;
            }
            if(n==2){
                break;
            }
        }
        return ans;
    }
}