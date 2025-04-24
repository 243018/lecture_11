def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 2) + recursive_nth_fibo(n - 1)


def main():
    value = 4
    sequence = [recursive_nth_fibo(n) for n in range(value + 1)]
    print(sequence)


if __name__ == "__main__":
    main()
