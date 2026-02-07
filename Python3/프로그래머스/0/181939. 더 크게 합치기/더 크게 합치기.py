def solution(a, b):
    result1 = str(a) + str(b)
    result2 = str(b) + str(a)
    if int(result2) > int(result1):
        answer = int(result2)
    else:
        answer = int(result1)
    return answer