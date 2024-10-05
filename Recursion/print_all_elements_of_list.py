l = [10,20,30,40,50]

def print_list(index):
    if(index<0):
        return 
    print_list(index-1)
    print(l[index])

print_list(len(l)-1)

