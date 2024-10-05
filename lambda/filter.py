def is_even(n):
    return n%2==0
l = [1,2,5,8,9]

evens = list(filter(is_even,l))

print(evens)


def is_even(n):
    return n%2==0
l = [1,2,5,8,9]

evens = list(filter(lambda n:n%2==0,l))

print(evens)