def solution(n):
    a = [i for i in range(1,1000000) if n % i == 1]
    return min(a)