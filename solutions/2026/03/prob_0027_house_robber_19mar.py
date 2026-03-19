def houseRobber(nums: List[int]) -> int:
    def helper(start, end):
        if start >= end:
            return 0
        if start == end - 1:
            return nums[start]
        dp = [0] * (end - start + 1)
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[end])
        for i in range(2, end - start + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[start+i])
        return dp[-1]

    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        return max(helper(0, n - 1), helper(1, n))