class Solution {
    boolean dfs(int i,int p,List<List<Integer>> adj,int[] vis,int[] pathVis){
        vis[i]=1;
        pathVis[i]=1;
        for(int k:adj.get(i)){
            if(vis[k]==0){
               if(dfs(k,i,adj,vis,pathVis))
                 return true;
            }
            else if(vis[k]==1 && pathVis[k]==1)
               return true;
        }
        pathVis[i]=0;
        return false;
    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj=new ArrayList<>();
        int v=numCourses;
        for(int i=0;i<v;i++){
            adj.add(new ArrayList<>());
        }
        int e=prerequisites.length;
        for(int i=0;i<e;i++){
           adj.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        int[] vis=new int[v];
        int[] pathVis=new int[v];

        for(int i=0;i<v;i++){
            if(vis[i]==0){
                if(dfs(i,-1,adj,vis,pathVis))
                   return false;
            }
        }

        return true;
    }
}