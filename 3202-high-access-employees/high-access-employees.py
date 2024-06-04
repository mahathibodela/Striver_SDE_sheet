class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """

        access_times.sort()
        print(access_times)
        temp = []
        for a, b in access_times:
            if b[0] == 0:
                b = b[1:]
            t = [a]
            t.append(int(b[:len(b) - 2]))
            t.append(int(b[len(b) -2 : len(b)]))
            temp.append(t)
        
        l = 0
        r = 1
        n = len(temp)
        ans = []
        mm = (temp[0][2] + 59) % 60
        mh = temp[0][1] + (temp[0][2] + 59) / 60 
        print(mh, mm)

        while r < n:
          
            if temp[l][0] == temp[r][0]:
                h, m = temp[r][1], temp[r][2]
                if not (h < mh or (h == mh and m <= mm)):
                    while l < r:
                        l += 1
                        mm = (temp[l][2] + 59) % 60
                        mh = temp[l][1] + (temp[l][2] + 59) / 60 
                        if h < mh or (h == mh and m <= mm):
                            break
                
                if r - l + 1 >= 3:
                    ans.append(temp[r][0])
                    c = temp[r][0]
                    while r + 1 < n and temp[r + 1][0] == c:
                        r += 1


            else:
                l = r
                mm = (temp[l][2] + 59) % 60
                mh = temp[l][1] + (temp[l][2] + 59) / 60 
            
            r += 1
            
        return ans
       