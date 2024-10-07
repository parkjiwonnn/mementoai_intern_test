# 1번 문제(x만큼 간격이 있는 n개의 숫자)

def solution(x, n):
    return [x*(i+1) for i in range(n)]
  
# x*(i+1) 연산: O(1)
# for문: O(n)
# solution 함수 시간 복잡도: O(n)