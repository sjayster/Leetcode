"""
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Base: If n < 3, there are no prime numbers (2 is not included)
1. We populate an array of True's for n numbers
2. Set primes[0] = primes[1] = False (as we know these are not primes)
3. In order to reduce the size of n, from the above theorem, it is enough if we iterate up to sqrt(n) + 1.
4. To simplify it even further, it is enough if we just use the primes in the list.
5. THIS IS WHERE I MADE A MISTAKE -> instead of iterating j over a range(2, n/i +1), I iterated over 2,n/2 +1, which caused a timeout error.
6. The reason we iterate over 2 to n/i is because, the previous primes would have already covered the remaining part of the list
7. If i*j is < our given n, we set primes[i*j] to False
8. Finally, return the sum of the array -> sum(True)

Another solution that was very interesting was,
https://discuss.leetcode.com/topic/14036/fast-python-solution

"""


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**(0.5)) + 1):
            if primes[i] == True:
                for j in range(2, n / i + 1):
                    if i * j < n:
                        primes[i * j] = False
        return sum(primes)
