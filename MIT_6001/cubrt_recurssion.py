def cubrt_iter(x, guess):
    if (abs(x - (guess * guess * guess)) <= 0.0000001):
        return guess
    else:
        guess = improve_guess(x, guess)
        print(guess)
        cubrt_iter(x, guess)



def improve_guess(x, guess):
    return float((guess + x / guess) / 2)


def sqrt(x):
    ans = sqrt_iter(x,1)
    return ans


sqrt(2)
