class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = defaultdict(int)
        for num in nums:
            n[num] = n[num]+1

        # the same above can be accomplished by Counter(nums)
        pq = []
        for key,v in n.items():
            heapq.heappush(pq,(-v,key))
        a = []
        for i in range(k):
            value, key = heapq.heappop(pq)
            a.append(key)
        return a
        