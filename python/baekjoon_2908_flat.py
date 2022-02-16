# from https://www.acmicpc.net/problem/1152
# - 문제 파악
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 
# 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# - 주요 단어 영문 이름 선정 
# 거꾸로 읽는다 -> reverse
# 두 수 -> first, second
# 큰 수 -> max

# - 테스트 케이스
# 734 893   -> 437
# 221 231   -> 132
# 839 237   -> 938

def main():
    # 두 수 받기
    first, second = input().split()
    # first, second = str(734), str(893)
    # first, second = str(221), str(231)
    # first, second = str(839), str(237)

    # 받은 두 수를 거꾸로 읽기
    reverse_fist = str()
    for char in first:
        reverse_fist = char + reverse_fist
    # for char in first[::-1]:      # other way
    #     reverse_fist += char
    
    reverse_second = str()
    for char in second:
        reverse_second = char + reverse_second

    # 두 수 비교해 큰 수 찾기
    max = int()
    if int(reverse_fist) > int(reverse_second):
        max = reverse_fist
    else :
        max = reverse_second

    # 큰 수 화면 표시하기
    print(max)
    pass

if __name__ == '__main__':
    main()