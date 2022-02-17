# from https://www.acmicpc.net/problem/1316
# - 실패 시 원인 기록
# + 

# - 문제 파악
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# - 유추 파악
#

# - 주요 단어 영문 이름 선정 
# 그룹 단어 -> group_word
# 단어      -> word
# 모든 문자 -> words
# 각 문자   -> char
# 연속      -> coutinus
# 단어 횟수 새기    -> count : from flow

# - 테스트 케이스
# 3 - happy new year    -> 3
# 4 - aba abab abcabc a -> 1
# 5 - ab aa aca ba bb   -> 4
# 2 - yzyzy zyzyz       -> 0
# 1 - z                 -> 1

import re
def main():
    #- flow    
    # 단어 갯수와 갯수만큼 단어 받음
    count = int(input())
    word_list = list()
    for _ in range(count):
        word_list.append(input())
    # word_list = ['happy', 'new', 'year']
    # word_list = ['aba', 'abab', 'abcabc', 'a']
    # word_list = ['ab', 'aa', 'aca', 'ba', 'bb']
    # word_list = ['yzyzy', 'zyzyz']
    # word_list = ['z']
    
    # 받은 단어 갯수만큼 돌면서, 
    group_word_count = int()
    for word in word_list:
        # 단어 내 그룹 단어 횟수 새기(try-on)
        char_count = int()
        for char in word:
            regexp = r'['+char+']+'
            temp_list = re.findall(regexp,word)
            if len(temp_list) > 1:
                break
            char_count += 1
        if char_count == len(word):
            group_word_count += 1

    # 단어 횟수 표시
    print(group_word_count)
    
    pass

if __name__ == '__main__':
    main()