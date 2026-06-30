sum = 0
count = 0

for num in range(1, 501):
    a = num
    arm = 0

    while a > 0:
        digit = a % 10
        arm = arm + digit**3
        a = a // 10

    if arm == num:
        sum = sum + num
        count = count + 1

print("Average =", sum / count)