import math
import csv

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def sequence(limit):
    results = []

    for n in range(3, limit + 1):
        k = 1
        while True:
            left = n - k
            right = n + k

            if is_prime(left) and (right > 3 and not is_prime(right)):
                results.append((n, k))
                break

            k += 1

    return results


def save_csv(data, filename="sequence_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "a(n)"])
        writer.writerows(data)


if __name__ == "__main__":
    LIMIT = 100000
    data = sequence(LIMIT)
    save_csv(data)

    print("Computed", len(data), "terms")
    print("Saved to sequence_results.csv")
