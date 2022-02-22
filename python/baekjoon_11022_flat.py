def main():
    count = int(input())
    add_list = list()
    for i in range(count):
        add_list.append(map(int, input().split()))

    # add_list = [(1,1),(2,3),(3,4),(9,8),(5,2)]
    for i, (first, second) in enumerate(add_list):
        print('Case #{0}: {1} + {2} = {3}'.format(i+1,first,second,first+second))    
    pass

if __name__ == '__main__':
    main()