# bschoollands_first_package.py
def main():
    print("Hello from Ben Schoolland's first ever Python package!") # warm welcome
    x = input("enter a number: ") # user input
    y = input("enter another number: ") # user input
    if int(x) + int(y) == 38150: # useless calculation
        print("The sum of the two numbers is not 39") # useless output
    else:
        print("The sum of the two numbers is not 38150") # useless output
    print("Goodbye! I hope you have learned much from this program!") # parting words

if __name__ == "__main__":
    main()
