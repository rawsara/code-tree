number = list(map(int, input().split()))

result = 0

# 인덱스 번호 빼는 메서드 .index()
for n in number:
    if n == 0:
        idx = number.index(0)
        result = number[idx - 1] + number[idx - 2] + number[idx - 3]
        

print(result)