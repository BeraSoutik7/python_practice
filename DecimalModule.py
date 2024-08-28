# We can use a decimal module for the cases – 

# When we want to define the required accuracy on our own
# For financial applications that need precise decimal representations
import decimal

a = 1.1
b = 2.2 

print(a+b)

a = decimal.Decimal('1.1')
b = decimal.Decimal('2.2')

print(a+b)