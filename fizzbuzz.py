# fizz buzz!

for num in xrange(1,100):
    msg = ''
    if num %3 == 0:
        msg += 'Fizz'
    if num %5 == 0:
        msg += 'Buzz'
    # if not msg:
    #     msg += str(num)
    print msg or num
