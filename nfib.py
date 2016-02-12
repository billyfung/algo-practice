# finding nth fibonnaci number


def fib(n):
    # start from the 0th fib and work way up
    if n < 0:
        raise Exception("Invalid number")
    elif n in [0,1]:
        return n

    previous = 0
    previous_previous = 0

    for _ in xrange(n):
        current = previous + previous_previous
        previous_previous = previous
        previous = current

    return current