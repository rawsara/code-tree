number = input()


# print(number) 스트링임

number =list(map(int,number.split(" ")))
# print(type(number))
# print(number)
sum_number = number[2] +number[4]+number[9]
print(sum_number)