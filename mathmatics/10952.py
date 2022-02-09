# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력:            출력
#       11              2
#       22              4
#       33              6
#       44              8
#       00                



while 1:
    a,b=map(int,input("숫자를 압력").split())
    if a==0 and b==0:
        break
    else:
        print(a+b)