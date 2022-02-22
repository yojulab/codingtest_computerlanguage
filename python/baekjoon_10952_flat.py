def main():
    # value_list = [(1,1),(2,3),(3,4),(9,8),(5,2),(0,0),]
    # index = -1
    while True:
        first, second = map(int,input().split())
        # index += 1
        # first, second = value_list[index]
        if first <= 0 and second <= 0:
            break
        print(first+second)    
    pass

if __name__ == '__main__':
    main()