#  1、问题分析
#  2、算法设计
#  3、算法分析
#  4、算法改进
import math


def prime(num):
    if num > 2:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        else:
            return True
    elif num == 2:
        return True
    else:
        return False


if __name__ == '__main__':
    # print(prime(49))
    primes = set()
    for j in range(2, 2002, 2):
        for n in range(2, j):
            if prime(n):
                primes.add(n)
                if (j - n) in primes or prime(j - n):
                    primes.add(j - n)
                    if n <= j - n:
                        print("{} = {} + {}".format(j, n, j - n))

    print("程序结束")
    print(sorted(primes))


