import random
user_input = int(input("Geben Sie eine Ganzzahl ein: "))
#random_zahl = random.randint(1,10)

def odd(zahl):
    return (zahl*3)+1

def even(zahl):
    return zahl/2

def main():
    zahl=7
    x = 0
    while x < user_input:
        if zahl%2==0:
            zahl = even(zahl)
        else:
            zahl = odd(zahl)
        print(zahl)
        x+=1

main()
