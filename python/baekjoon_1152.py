# from https://www.acmicpc.net/problem/1152
# - 문제 파악
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

# - 주요 단어 영문 이름 선정 
# 문자열 -> words
# 한 단어 -> word
# 횟수 -> count

# - 테스트 케이스
# The Curious Case of Benjamin Button -> 6
# The first character is a blank -> 6
# The last character is a blank -> 6

def main():
    # 문자열 받기
    words = input()
    # words = 'The Curious Case of Benjamin Button'
    # words = 'The first character is a blank'
    # words = 'The last character is a blank'

    # 단어 숫자 세기
    word_list = words.split()

    # 횟수 출력
    count = len(word_list)
    print(count)
    pass

if __name__ == '__main__':
    main()