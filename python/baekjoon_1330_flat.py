def main():
    first, second = input().split()
    A = int(first)
    B = int(second)
    if A > B:
        print('>')
    elif A < B :
        print('<')
    elif A == B :
        print('==')    
    else :
        print('?')    
    pass

if __name__ == '__main__':
    main()