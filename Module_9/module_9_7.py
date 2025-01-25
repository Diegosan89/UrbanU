# Декораторы

def is_prime(function):
    def wrapper(a, b, c):
        result_ = sum((a, b, c))

        is_prime_ = True
        for j in range(2, int(result_ ** 0.5 + 1)):
            if result_ % j == 0:
                print('число составное')
                is_prime_ = False
                break

        if is_prime_ and result_ != 1:
            print('число простое')

        return result_

    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum((a, b, c))


result = sum_three(2, 3, 6)
print(result)
