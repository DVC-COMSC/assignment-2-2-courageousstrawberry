def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celcius = float(input('Enter a temperature in Celcius: '))
    fahrenheit = (9*celcius)/5 + 32

    print(f'The temperature in fahrenheit is: {fahrenheit:.2f}')

    return celcius, fahrenheit

if __name__ == '__main__':
    main()
