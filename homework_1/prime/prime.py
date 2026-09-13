"""Задача 3. Количество простых чисел, меньших N. Решето Эратосфена."""


def count_primes(n: int) -> int:
    """Сколько существует простых чисел p, для которых p < n."""
    if n < 3:
        return 0

    # is_prime[i] относится к числу i, рассматриваем числа от 0 до n - 1.
    is_prime = bytearray([1]) * n
    is_prime[0] = is_prime[1] = 0

    p = 2
    while p * p < n:
        if is_prime[p]:
            # Кратные меньше p * p уже вычеркнуты меньшими делителями.
            is_prime[p * p:n:p] = bytearray(len(range(p * p, n, p)))
        p += 1

    return sum(is_prime)


def main() -> None:
    print(count_primes(int(input().strip())))


if __name__ == "__main__":
    main()
