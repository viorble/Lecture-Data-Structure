def countdown_loop(i):
    for i in range(i, 0, -1):
        print(i)


def countdown_recursion(i):
    # base case
    print(i)
    if i <= 1:
        return
    # recursive case
    else:
        countdown_recursion(i - 1)


print("Countdown using loop")
countdown_loop(5)

print("Countdown using recursion")
countdown_recursion(5)
