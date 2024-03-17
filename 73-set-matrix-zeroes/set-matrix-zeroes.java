class Solution {
    public void setZeroes(int[][] matrix) {
         Set<Integer> rs = new LinkedHashSet<Integer>();   
         Set<Integer> cs = new LinkedHashSet<Integer>();

         int m=matrix.length;
         int n=matrix[0].length;

         for(int i=0;i<m;i++){
             for(int j=0;j<n;j++){
                 if(matrix[i][j]==0){
                     rs.add(i);
                     cs.add(j);
                 }
             }
         }

         for(int i=0;i<m;i++){
             for(int j=0;j<n;j++){
                 if(rs.contains(i) || cs.contains(j))
                     matrix[i][j]=0;
             }
         }
    }
}