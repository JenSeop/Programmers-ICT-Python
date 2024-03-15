def solution(str1, str2, s):
    return str1[:s] + str2 + str1[len(str2) + s:]