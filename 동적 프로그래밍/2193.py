# 재귀함수를 활용한 이친수 구하기 문제

# 1,1,2,3,5,8,13,21... 순이다.

N= int(input())
array =  [ 0 for _ in  range (N+1)]
array[0]=1
array[1]=1
array[2]=2
for i in  range (3,N+1):
    array[i]=array[i-1]+array[i-2]
print(array[N-1]) 