# git : 
def main():
    number_str = input()
    array = list()
    for char in number_str:
        array.append(int(char))

    # array = [2,1,4,3]    # 4321
    # array = [9,9,9,9,9,8,9,9,9] # 999999998
    # array = [6,1,4,2,3]     # 64321
    # array = [5,0,0,6,1,3,0,0,9] # 965310000
    array.sort(reverse=True)
    for number in array:
        print(number, end='')
    pass

if __name__ == '__main__':
    main()