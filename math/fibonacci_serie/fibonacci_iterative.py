n = int(input("Geben Sie eine Zahl ein, wielange der Fibonacci-Durchlauf gehen soll: "))
temp_erg = 0

if n <= 0:
    print("Zahl ist kleiner oder gleich Null, Ergebnis is 0.")
elif n==1:
    print("Zahl nach 1 Durchgang ist 1 da 0+1=1 ist.")
else:
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
        print(fib)
