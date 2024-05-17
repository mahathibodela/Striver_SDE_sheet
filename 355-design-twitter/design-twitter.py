class Twitter(object):

    def __init__(self):
        self.following = defaultdict(list)
        self.posts = defaultdict(list)
        self.time = 0 

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.posts[userId].append((self.time, tweetId))
        
        self.time -= 1
        return None

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        ans = []
        n = len(self.posts[userId])
        if n != 0:
            heap.append((self.posts[userId][n - 1], n-1, userId))
            
        if userId in self.following:
            for user in self.following[userId]:
                n = len(self.posts[user])
                if n != 0:
                    heap.append((self.posts[user][n - 1], n-1, user))
              
        
        heapq.heapify(heap)
        count = 10
       
        while count != 0 and len(heap) != 0:
            post, ind, user = heapq.heappop(heap)
            _, tweet = post
            ans.append(tweet)
            ind -= 1
            if ind >= 0 :
                heapq.heappush(heap, ((self.posts[user][ind], ind, user)))
            count -= 1
        self.time -= 1
        
        return ans




    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """

        if followerId in self.following and followeeId not in self.following[followerId] :
            self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]

        self.time -= 1
        return None

        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        self.time -= 1

        return None
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)