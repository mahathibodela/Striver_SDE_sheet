class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        long tot=0,ans=INT_MIN,sum=0;
        
        for(int i=0;i<nums.size();i++){
            tot=tot+nums[i];
            sum=sum+(i*nums[i]);
        }
        ans=max(ans,sum);

        for(int i=nums.size()-1;i>0;i--){
            sum=sum+tot-(nums.size()*nums[i]);
            ans=max(ans,sum);
        }

        return (int)ans;
    }
};