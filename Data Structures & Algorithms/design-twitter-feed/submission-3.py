class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # userId > [(timestamp, tweetId), ...]
        self.following = defaultdict(set) # userId > {followeeIds}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        #1. get all tweets from relevant users
        #2. return 10 tweetIds
        relevant_users = [userId] + list(self.following[userId])
        # print(relevant_users)
        
        all_tweets = [(-tweet[0], tweet[1]) for relevant_user in relevant_users for tweet in self.tweets[relevant_user]]
        heapq.heapify(all_tweets)
        
        res = []
        for _ in range(10):
            if not all_tweets:
                break
            curr = heapq.heappop(all_tweets)
            res.append(curr[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
