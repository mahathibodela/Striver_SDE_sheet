class Solution {
private:
    bool isOk(int i, int j, vector<string>& board){
        int n = board[0].length();

        // checking coloumn
        for(int k = i - 1; k >= 0; k --){
            if(board[k][j] == 'Q') return false;
        }

        //checking left diagnols
        int l = i - 1;
        int r = j - 1;
        while (l >= 0 && r >= 0){
            if(board[l][r] == 'Q') return false;
            l -= 1;
            r -= 1;
        }

        //checking right dianols
        l = i - 1;
        r = j + 1;
        while (l >= 0 and r < n){
            if(board[l][r] == 'Q') return false;
            l -= 1;
            r += 1;
        }

        return true;
    }
    void check(int r, vector<string>& board, vector<vector<string>>& ans, int n){
        if(r == n){
            ans.push_back(board);
            return ;
        }

        for(int i = 0; i < n; i++){
            if(board[r][i] == '.' && isOk(r, i, board)){
                board[r][i] = 'Q';
                check(r + 1, board, ans, n);
                board[r][i] = '.';
            }
        }

        return ;
    }
public:
    vector<vector<string>> solveNQueens(int n) {

        vector<vector<string>> ans;
        vector<string> board;
        string temp = "";
        for(int i = 0; i < n; i++) temp += '.';
        for(int i = 0; i < n; i++) board.push_back(temp);

        check(0, board, ans, n);
        return ans;    
    }
};