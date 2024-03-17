class Solution:
    def binsearch(self,arr,target,l,r):
        if l<=r:
            lr = l//len(arr[0])
            lc = l%len(arr[0])
            ur = r//len(arr[0])
            uc = r%len(arr[0])
            if(arr[lr][lc]==target): return True;
            if(arr[ur][uc]==target): return True
            mid = l + (r-l)//2
            ra = mid//len(arr[0])
            c = mid%len(arr[0])
            print(r,"and",c,"and",mid,"and",l,ra)
            if arr[ra][c]==target:
                print("here")
                return True
            elif arr[ra][c]>target:
                return self.binsearch(arr,target,l,mid-1)
            else:
                return self.binsearch(arr,target,mid+1,r)
        return False

    def searchMatrix(self, matrix, target):
        return self.binsearch(matrix,target,0,len(matrix)*len(matrix[0])-1)