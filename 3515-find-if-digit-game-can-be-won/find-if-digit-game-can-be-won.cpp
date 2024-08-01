class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int ss=0;
        int ds=0;
        for(int i=0;i<nums.size();i++){
            if (nums[i]<10){
                ss=ss+nums[i];
            }
            else{
                ds=ds+nums[i];
            }
        }
        if (ss!=ds){
            return true;
        }
        else{
            return false;
        }
        
    }
};