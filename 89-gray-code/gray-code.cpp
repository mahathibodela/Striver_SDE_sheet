class Solution {
public:
    vector<string> generate(int n){
        if(n == 1){
            return {"0", "1"};
        }

        vector<string> temp = generate(n - 1);
        vector<string> ans;
        for(string s:temp){
            ans.push_back("0" + s);
        }
        for(int i = temp.size() - 1; i >= 0; i --){
            ans.push_back("1" + temp[i]);
        }

        return ans;

    }

    vector<int> grayCode(int n) {
        vector<string> temp = generate(n);
        vector<int> ans;
        for(auto i: temp){
            ans.push_back(stoi(i, 0, 2));
        }

        return ans;
        
    }
};