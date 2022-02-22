def main():
    first = input()
    second = input()
    A= int(first)
    B, C, D = second[0], second[1], second[2]
    B = int(B)
    C = int(C)
    D = int(D)
    print(A*D)
    print(A*C)
    print(A*B)
    print(A*int(second))    
    pass

if __name__ == '__main__':
    main()