def fib(nth):
    if nth <= 0:
        return 0
    elif nth == 1:
        return 1
    return fib(nth-1) + fib(nth-2)

def better_fib(nth):
    if nth <= 0:
        return 0
    elif nth == 1:
        return 1
    current_nth = 1
    previous = 1
    current = 1
    while current_nth != nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1

    return current


for n in range(45):
    print(f'{n}: {better_fib(n)}')
