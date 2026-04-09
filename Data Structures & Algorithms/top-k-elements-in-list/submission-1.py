class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for i in nums:
            res[i] = res.get(i, 0) + 1
        arr = [[] for i in range(len(nums)+1)]
        for i,v in res.items():
            arr[v].append(i)
        res_list = []
        for i in range(len(arr)-1, 0, -1):
            for j in arr[i]:
                res_list.append(j)
                if len(res_list)==k:
                    return res_list
        return res_list