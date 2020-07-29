def cubrt_iter(x, guess):
    if (abs(x - (cube(guess))) <= 0.0000001):  #tolerance level should be considered, when testing x < 0.0000001, the current tolerance level can't be used as stop condition
        return guess
    else:
        guess = improve_guess(x, guess)
        print(guess)
        cubrt_iter(x, guess)


def improve_guess(x, guess):
    return float((2 * guess + x / sqr(guess)) / 3)

def sqr(x):
    sqr_x = x * x
    return sqr_x


def cube(x):
    cube_x = x * x * x
    return cube_x

def cubrt(x):
    ans = cubrt_iter(x, 1)
    return ans
    print(ans)

cubrt()