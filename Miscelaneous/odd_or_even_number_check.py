def even_or_odd(number):
    test = (number/2) % 1
    if test !=0:
        return 'odd'
    else:
        return 'even'

def input_function():
    while True:
        try:
            val = float(input('Please enter an interger'))
            if (val % 1) != 0:
                print('enter a number without decimal places')
                input_function()
            return val
            break
        except ValueError:
            print('Enter a numeric value, not a string')
    

input_val = input_function()
output_val = even_or_odd(input_val)
print(output_val)