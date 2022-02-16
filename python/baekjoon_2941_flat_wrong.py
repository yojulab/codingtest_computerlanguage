# from https://www.acmicpc.net/problem/2941
# - 실패 원인
# + 유추 파악 : ddz=z= -> 3 예제 보니 중복 크로아티아 알파벳은 1회로 처리 누락

# - 문제 파악
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
# 위 목록에 없는 알파벳은 한 글자씩 센다.

# - 유추 파악 
# 목록 보니 크로아티아 알파벳 한 자는 알파벳은 두 글자.

# - 주요 단어 영문 이름 선정 
# 단어 -> word
# 몇 개 -> count
# 크로아티아 알파벳 -> croatia_alphabet
# 알파벳 -> alphabet
# 목록 -> list
# 한 글자 -> char

# - 테스트 케이스
# ljes=njak   -> 6
# ddz=z=      -> 3
# nljj        -> 3
# c=c=        -> 2
# dz=ak       -> 3

def main():
    # 단어를 받음
    # word = input()
    # word = 'ljes=njak'
    word = 'ddz=z='
    # word = 'nljj'
    # word = 'c=c='
    # word = 'dz=ak'

    # 크로아티아 알파벳 목록 만듬
    croatia_alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    # 받은 단어에서 크로아티아 알파벳 갯수 확인, 중복은 1회로 처리
    croatia_alphabet_count = int()
    for idx in range(2,len(word)+1):
        two_word = word[idx-2:idx]
        if two_word in croatia_alphabet_list:
            croatia_alphabet_count += 1

    # 받은 단어에서 크로아티아 알파벳 뺀 갯수 확인
    croatia_alphabet_without_count = len(word) - (croatia_alphabet_count*2)
    count = croatia_alphabet_without_count + croatia_alphabet_count

    # 크로아티아 알파벳 넣은 갯수와 뺀 갯수 더해서 출력
    print(count)
    pass

if __name__ == '__main__':
    main()