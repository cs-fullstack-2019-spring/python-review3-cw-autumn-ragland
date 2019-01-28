# main function used to call prob1-4
def main():
    prob1()
    # prob2()
    # prob3()
    # bonus()

# Given a number n, return True if n is in the range 1..10, inclusive and the range is False
def prob1():
    num = int(input("Enter a number: "))
    out_of_range = True
    print(in1to10(num, out_of_range))
# check if the number is in the range and if the range is True or False
def in1to10(n, out_of_range):
    if out_of_range == False:
        if n <= 10 and n >= 1:
            return True
        else:
            return False
    else:
        if n <= 10 and n >= 1:
            return False
        else:
            return True
# Create a function that has a loop that quits with the equal sign.
# Print all the strings that were entered as one line with each word separated by a comma and space.
def prob2():
    inputList = []
    userInput = input("Enter a word: ")
    comma = ", "
    while userInput != "=":
        inputList.append(userInput)
        userInput = input("Great! Enter another word: ")
    print(comma.join(inputList))
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Print the result from your function.
def prob3():
    num = int(input("Enter a positive number: "))
    print(near_ten(num))
def near_ten(number):
    while number > 0:
        if number % 10 == 0:
            return True
        elif (number + 1) % 10 == 0:
            return True
        elif (number + 2) % 10 == 0:
            return True
        else:
            return False






if __name__ == '__main__':
    main()