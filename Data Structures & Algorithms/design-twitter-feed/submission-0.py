class Twitter:
    def __init__(self):
        self.followings = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        if userId not in self.followings[userId]:
            self.follow(userId, userId)

        for followeeId in self.followings[userId]:
            if followeeId not in self.tweets:
                continue

            index = len(self.tweets[followeeId]) - 1
            count, tweetId = self.tweets[followeeId][index]
            heap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(heap)

        while heap and len(res) < 10:
            _, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)