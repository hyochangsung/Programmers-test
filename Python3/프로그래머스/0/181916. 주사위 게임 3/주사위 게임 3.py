def solution(a, b, c, d):
    nums = [a, b, c, d]
    cnt = [nums.count(i) for i in nums]
    if max(cnt) == 4:
        return 1111 * a
    elif max(cnt) == 3:
        return (10 * nums[cnt.index(3)] + nums[cnt.index(1)]) ** 2
    elif max(cnt) == 2:
        if min(cnt) == 2:
            p = nums[cnt.index(2)]
            return (a + b) * abs(a - b) if a != b else (a + c) * abs(a - c) 
        else:
            p = nums[cnt.index(2)]
            return (a * b * c * d) / (p**2)
    else:
        return min(nums)