number = input()

if (len(number) != 10):
    print('Not a mobile number')
else:
    if (number[0] == '0' and (number[1] in ['6', '8', '9'])):
        print('Mobile number')