""" 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오. """

T = int(input())
for i in range(T):
    S = list(str(input()))
    min = S[0]
    max = S[-1]
    print("{}{}".format(min,max))