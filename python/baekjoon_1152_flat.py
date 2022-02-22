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