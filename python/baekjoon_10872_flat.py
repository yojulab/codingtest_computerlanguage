# - 테스트 케이스
# 10  -> 3628800
# 0   -> 1
# 3   -> 6 : from 프로그래밍 순서

def main():
    # 정수를 입력 받음
    integer = int(input())
    # integer = 10
    # integer = 0
    # integer = 3

    # 입력된 정수보다 작은 모든 양수를 곱함.
    factorial_integer = 1
    for number in range(integer, 0, -1):
        factorial_integer *= number
    
    # 모두 곱한 값 표시
    print(factorial_integer)
    pass

if __name__ == '__main__':
    main()