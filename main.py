def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    Code Your Program here
    """
    if num1 > num2 and num1 > num3:
        maxnum = num1
    
    elif num2 > num1 and num2 > num3:
        maxnum = num2
    
    elif num3 > num1 and num3 > num2:
        maxnum = num3

    print(f'The greates number is {maxnum}')
    ########################################
    # Do not delete the return statement
    ########################################
    return maxnum


if __name__ == '__main__':
    main()
