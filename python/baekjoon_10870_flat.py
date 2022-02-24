def main():
    # 피보나치 수 받기(n ≥ 2)
    number = int(input())
    # number = 10  # 55
    # number = 17  # 1597

    # 피보나치 수 찾기(Fn = Fn-1 + Fn-2)
    fibonacci_before = 0
    fibonacci_after = 1
    fibonacci_number = number
    for i in range(2, number+1):
        fibonacci_number = fibonacci_before + fibonacci_after
        fibonacci_before = fibonacci_after
        fibonacci_after = fibonacci_number

    # 계산된 피보나치 수 표시
    print(fibonacci_number)

    pass

if __name__ == '__main__':
    main()