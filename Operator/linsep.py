a=input()
b=int(input())
c=int(input())
d=int(input())
arrow = (d * a) + '>'
print(arrow, end='')

line_break = b * '\n'
print(end=line_break)

seperator = c * ' '
print(seperator + arrow, end='')

print(end=line_break)

print(arrow)