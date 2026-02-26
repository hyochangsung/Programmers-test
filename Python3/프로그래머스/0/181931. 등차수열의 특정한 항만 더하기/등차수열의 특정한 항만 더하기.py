def solution(a, d, included):
    total = 0
    for i in range(len(included)):
        if included[i]:
            total += a + d*i
    answer = total
    return answer