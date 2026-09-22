class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -1 * abs(a - b))
        print(stones)
        return 0 if len(stones) == 0 else stones[0] * -1
