numbers = list(map(int, input().split()))

# 홀수 번째 입력받은 정수의 합
odd =  sum(numbers[::2])
# 짝수 번째 입력받은 정수의 합
even = sum(numbers[1::2])

if odd > even:
    result = odd - even
else:
    result = even - odd

print(result)