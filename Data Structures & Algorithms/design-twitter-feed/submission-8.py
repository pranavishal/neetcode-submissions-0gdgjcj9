from collections import deque
import heapq
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.tweets[userId].append((-self.timer, tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_lists = []
        tweet_lists.append(self.tweets[userId])
        for user in self.following[userId]:
            tweet_lists.append(self.tweets[user])
        
        #print(tweet_lists)
        tweet_heap = []
        tweet_feed = []
        for tw_list in tweet_lists:
            if tw_list:
                counter, tweet, userId = tw_list[-1]
                heapq.heappush(tweet_heap, (counter, tweet, -1, userId))
        
        while len(tweet_feed) < 10 and tweet_heap:
            counter, tweetId, index, userId = heapq.heappop(tweet_heap)
            tweet_feed.append(tweetId)

            index -= 1
            if abs(index) <= len(self.tweets[userId]):
                counter, tweet, userId = self.tweets[userId][index]
                heapq.heappush(tweet_heap, (counter, tweet, index, userId))
        
        return tweet_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
