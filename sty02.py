## 입력 받은 정수를 더하기
## (-)음수 입력시 중단 후 계산한 값 출력

hap = 0
while True:
    num = int(input())
    if num<0:
        break
    else :
        hap = hap + num
print(hap)