
def main ():

    # What is the largest prime number factor of the entered number?

    number = int(input("Please enter a number: " ))

    for a in range(2, number+1):
        if number % a == 0:
            prime = True
            for b in range(2, (a // 2 + 1)):
                if a % b == 0:
                    prime = False
                    break

            if prime == True:
                print(a, "is a prime factor of ", number)

if __name__ == '__main__':
    main()