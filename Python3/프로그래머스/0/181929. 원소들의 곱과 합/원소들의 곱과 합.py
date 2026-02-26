def solution(num_list):
    s_total = 0
    m_total = 1
    for i in num_list:
        m_total *= i
        s_total += i
    if m_total < (s_total ** 2):
        answer = 1
    else:
        answer = 0
    return answer