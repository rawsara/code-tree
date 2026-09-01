number = list(map(int,input().split()))

# 짝수번째 숫자만 슬라이싱 후 합계 sum
sum_number = sum(number[1::2])

# 3의 배수 번째로 입력된 값들만 슬라이싱
slice_number = number[2::3]
avg_number = sum(slice_number)/len(slice_number)

# 소수점 첫째짜리까지 표기, 프린트에서 :.1f, 두째짜리면 :.2f
print(f'{sum_number} {avg_number:.1f}')
