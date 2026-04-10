import heapq
from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweet_feed = defaultdict(list)
        self.tweets = defaultdict(deque)
        self.counter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        for user in self.followers[userId]:
            heapq.heappush(self.tweet_feed[user], (-self.counter, -tweetId, userId))

        heapq.heappush(self.tweet_feed[userId], (-self.counter, -tweetId, userId))
        self.tweets[userId].appendleft((-self.counter, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        results = set()
        temp = []
        while self.tweet_feed[userId] and len(results) < 10:
            counter, tweet, user = heapq.heappop(self.tweet_feed[userId])
            if userId == user or userId in self.followers[user]:
                results.add((-counter, -tweet))
                temp.append((counter, tweet, user))
        
        for tweets in temp:
            heapq.heappush(self.tweet_feed[userId], tweets)
        
        output = list(results)
        output.sort(key=lambda x: x[0], reverse=True)
        final = []
        for out in output:
            final.append(out[1])
        return final
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followeeId].add(followerId)
        self.followers[followeeId].add(followeeId)

        counter = 0
        for tweet in self.tweets[followeeId]:
            heapq.heappush(self.tweet_feed[followerId], (tweet[0], -tweet[1], followeeId))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].discard(followerId)
        
