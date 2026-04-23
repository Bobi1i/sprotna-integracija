def deli(a, b):
    if b == 0:
        raise ValueError("Deljenje z nič ni dovoljeno!")
    return a / b
 
 
if __name__ == "__main__":
    print(deli(10, 2))
    print(deli(12, 6))