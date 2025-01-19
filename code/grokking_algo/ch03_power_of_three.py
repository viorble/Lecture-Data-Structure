def is_power_of_three_recursion(n):
    if n < 1:
        return False
    if n == 1:
        return True
    elif n % 3 == 0:
        return is_power_of_three_recursion(n // 3)
    else:
        return False


def is_power_of_three_loop(n):
    if n < 1:
        return False

    # 不斷地用 3 去除 n，直到無法整除為止
    while n % 3 == 0:
        n //= 3

    # 如果最後的結果為 1，則 n 是 3 的次方
    return n == 1


def is_power_of_three_math(n):
    import math

    if n < 1:
        return False

    # 計算以 3 為底的對數並檢查結果是否為整數
    log_result = math.log(n, 3)
    return log_result.is_integer()


# 測試範例
test_cases = [-10, 0, 1, 9, 45]

print("Using recursion")
for num in test_cases:
    print(f"Is {num} a power of three? {is_power_of_three_recursion(num)}")

print("Using loop")
for num in test_cases:
    print(f"Is {num} a power of three? {is_power_of_three_loop(num)}")

print("Using math")
for num in test_cases:
    print(f"Is {num} a power of three? {is_power_of_three_math(num)}")
