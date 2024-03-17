class Solution {
    public void rotate(int[][] matrix) {
        //transpose karke karna beta and reverse it -- hogaya kahani
        int m=matrix.length;
        int n=matrix[0].length;
        int[][] nm=new int[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                nm[i][j]=matrix[i][j];
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                matrix[i][j]=nm[m-j-1][i];
            }
        }
    }
}