a = int(input('enter the num : '))
b = int(input('enter the num : '))
c =input('add/sub/mul/div : ')
add = a+b
sub = a-b
mul = a*b
div = a/b
if (c == 'add'):
    print('the final value is : ',add)
if (c == 'sub'):
    print('the final value is : ',sub)
if (c == 'mul'):
    print('the final value is : ',mul)
if (c == 'div'):
    print('the final value is : ',div)
else:
    print('invalid')
