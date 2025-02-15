num = int(input('enter the number:'))
original_num = num
s = 0
order = len(str(num))
for digit in str(num):
    s += int(digit)**order
if num == s:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
            
