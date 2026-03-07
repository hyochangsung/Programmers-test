def solution(my_string, is_prefix):
    prefix = [my_string[:i] for i in range(len(my_string))]
    if is_prefix in prefix:
        return 1
    else:
        return 0