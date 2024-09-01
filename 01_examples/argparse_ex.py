import math
import argparse

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Calculates the least common multiple of A and B")
    parser.add_argument('--verbose', '-v', help='Verbose output', action="store_true")
    parser.add_argument('A', help='First number', type=int)
    parser.add_argument('B', help='Second number', type=int)
    args = parser.parse_args()

    if args.verbose:
        print(f"The LCD of {args.A} and {args.B} is: {math.lcm(args.A, args.B)}")
    else:
        print(math.lcm(args.A, args.B))
