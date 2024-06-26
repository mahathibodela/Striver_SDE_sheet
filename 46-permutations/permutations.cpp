class Solution {
private:

void swap(vector<int>& nums, int i, int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

void check(int ind, vector<int>& nums, vector<vector<int>>& ans, int n){
    if(ind == n - 1){
        ans.push_back(nums);
        return ;
    }

    for(int i = ind; i < n; i ++){
        swap(nums, i, ind);
        check(ind + 1, nums, ans, n);
        swap(nums, i, ind);
    }

    return ;
}


public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = nums.size();
        check(0, nums, ans, n);
        return ans;     
    }
};