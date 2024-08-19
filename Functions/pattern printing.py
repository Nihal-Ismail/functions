# def pattern_print(n):
#     if n % 2 == 0:
#         # If n is even, print the flipped pattern
#         for i in range(n, 0, -1):
#             print('* ' * i)
#     else:
#         # If n is odd, print the normal pattern
#         for i in range(1, n + 1):
#             print('* ' * i)
#


def pattern_print(n):
    if n % 2==0:
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end=" ")
            print()
    else:
        for i in range(1,n+1):
            for j in range(i):
                print("*",end=" ")
            print()


# Example usage
n = int(input("Enter the number of rows (n): "))
pattern_print(n)