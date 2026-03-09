def solution(my_string, m, c):
    answer = ''
    rows = [my_string[i:i+m] for i in range(0,len(my_string),m)]
    for row in rows:
        answer += row[c-1]
    return answer