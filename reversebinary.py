def reversebinary():
    x = int(input())
    print int( bin(x)[2:][::-1],2)

if __name__ == "__main__":
    reversebinary()