import math
# O(log n)
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a%b)

if __name__ == "__main__":
    print(f"gcd(758, 306) = {gcd(758, 306)}")
    print(f"gcd(96, 36) = {gcd(96, 36)}")
    print(f"gcd(56, 20) = {gcd(56, 20)}")
    print(f"gcd(198, 256) = {gcd(198, 256)}")
    print(f"gcd(1236, 12) = {gcd(1236, 12)}")
    print(f"gcd(546, 23) = {gcd(546, 23)}")
    print(f"gcd(12, 105) = {gcd(12, 105)}")
    print(f"gcd(15489, 156) = {gcd(15489, 156)}")
    print(f"gcd(1723, 5) = {gcd(1723, 5)}")
    print(f"gcd(96, 76) = {gcd(96, 76)}")
    print(f"gcd(7, 3) = {gcd(7, 3)}")