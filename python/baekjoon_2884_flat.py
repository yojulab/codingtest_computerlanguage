def main():
    first, second = input().split() #  map(int, input().split())
# temp_list = [(10,10),(0,30),(23,40),(20,45),(9,45),]
# for first, second in temp_list:
    hour = int(first)
    minus = int(second)
    if minus >= 45:
        print(hour, minus-45)
    elif minus < 45 and hour > 0:
        print(hour-1, minus+15)
    else :
        print(hour+24-1, minus+15)
    pass

if __name__ == '__main__':
    main()