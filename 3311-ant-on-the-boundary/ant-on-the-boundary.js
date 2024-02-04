/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let ans=0
    let cnt=0
    for(let i=0;i<nums.length;i++){
        ans+=nums[i]
        if (ans==0){
            cnt+=1
        }
    }
    return cnt
    
};