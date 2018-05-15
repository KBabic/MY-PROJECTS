# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
d = input('Enter a digit: ')
x = d + '+' + d*2 + '+' + d*3 + '+' + d*4
print(x)
y = x.split('+')
sum = 0
for num in y:
    sum += int(num)
print(sum)

# another way:
# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print (n1+n2+n3+n4)
