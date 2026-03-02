def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        candidate = [arr[i] for i in range(s,e+1) if arr[i] > k]
        answer.append(min(candidate) if candidate else -1) 
    return answer