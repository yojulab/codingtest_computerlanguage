# - 테스트 케이스
# ljes=njak   -> 6
# ddz=z=      -> 3
# nljj        -> 3
# c=c=        -> 2
# dz=ak       -> 3

def main():
    # 단어를 받음    
    word = input()
    # word = 'ljes=njak'
    # word = 'ddz=z='
    # word = 'nljj'
    # word = 'c=c='
    # word = 'dz=ak'

    # 크로아티아 알파벳 목록 만듬
    croatia_alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    # 받은 단어에서 크로아티아 알파벳 확인 후 한 자('?')로 변환
    for croatia_alphabet in croatia_alphabet_list:
        word = word.replace(croatia_alphabet, '?')

    # word 문자 수 확인 후 출력
    count = len(word)
    print(count)
    pass

if __name__ == '__main__':
    main()