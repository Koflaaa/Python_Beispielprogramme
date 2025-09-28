def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
def main():
    n = int(input("Wie viele Fibonacci-Zahlen sollen berechnet werden: "))
    reihe = []
    for i in range(n):
        reihe.append(fibonacci_rec(i))
    print(f"Die ersten {n} Fibonacci-Zahlen:")
    print(reihe)
    
main()
