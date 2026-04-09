class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_1 = []
        k = 1
        for i in nums:
            k = k * i
            arr_1.append(k)
        arr_2 = [0] * len(nums)
        k = 1
        for i in range(len(nums), 0, -1):
            k = k * nums[i-1]
            arr_2[i-1] = k
        # [1, 2 , 8, 48]
        # [48, 48, 24, 6]
        arr_3 = [0] * len(nums)

        arr_3[0] = arr_2[1]
        
        arr_3[len(nums)-1] = arr_1[len(nums)-2]
        
        for i in range(1, len(nums)-1):
            arr_3[i] = arr_1[i-1] * arr_2[i+1]
        
        return arr_3
