
if __name__ == "__main__":
    print("Hello bits :D")
    a = 0b110
    b = 9
    print(f"a = {a} = {bin(a)}")
    print(f"b = {b} = {bin(b)}")

    print(f"a << 2 = {a << 2} = {bin(a << 2)}")
    print(f"b << 1 = {b << 1} = {bin(b << 1)}")

    print(f"a >> 1 = {a >> 1} = {bin(a >> 1)}")
    print(f"b >> 1 = {b >> 1} = {bin(b >> 1)}")

    print(f"~a = {~a} = {bin(~a)}")
    print(f"~b = {~b} = {bin(~b)}")

    print(f"a & b = {a & b} = {bin(a & b)}")
    print(f"a | b = {a | b} = {bin(a | b)}")
    print(f"a ^ b = {a ^ b} = {bin(a ^ b)}")