""" 단어 $S$와 정수 $i$가 주어졌을 때, $S$의 $i$번째 글자를 출력하는 프로그램을 작성하시오. """

S = str(input())
i = int(input())
list = list(S)
print(list[i-1])