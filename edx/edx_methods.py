'''
# This function returns a list, containing all
# the devisors of the parameter.
def find_devisors(k):
    list_devisors=[]
    for number in range(1,k+1):
        if k%number==0:
            list_devisors.append(number)
    return list_devisors

# This function returns a list, containing the sorted
# cube root values of all numbers from 1 to the parameter.
def cube_root_list(k):
    list_cube_root=[]
    if k<=1:
        return list_cube_root
    else:
        for numbers in range(1, k):
            cube_root_numbers=numbers**(1/3)
            list_cube_root.append(cube_root_numbers)
    return list_cube_root

# This function returns a list, containing the
# odd numbers between the two paramters.
def return_even_numbers(a,b):
    list_even_numbers=[]
    if b>a:
        for numbers in range(a,b+1):
            if numbers%2==0:
                pass
            else:
                list_even_numbers.insert(0, numbers)
    return list_even_numbers

# This function returns a list, containing the
# even numbers between the two parameters.
def return_even_numbers(a,b):
    list_even_numbers=[]
    for numbers in range(a,b):
        if numbers%2==0:
            list_even_numbers.append(numbers)
    return list_even_numbers

# This function return a list, containing the first
# five multiples of the parameter.
def return_multiples(k):
    list_multiple=[]
    list_multiple.append(k*1)
    list_multiple.append(k*2)
    list_multiple.append(k*3)
    list_multiple.append(k*4)
    list_multiple.append(k*5)
    return list_multiple

user_list=['doge', 'cat', 3, 8.9]
user_list.insert(1, 'birb')
print(user_list)
user_list.append('snek')
print(user_list)
user_list.pop(2)
print(user_list)
user_list.remove('birb')
print(user_list)
variable=user_list.pop(0)
print(variable)

MyList = [3, "dog", 9, "cat"]
MyList.extend([7,8])
print (MyList)

my_list = []
steps_plus_from_integer=3
from_integer=2
to_integer=30
for x in range(from_integer,to_integer,steps_plus_from_integer):
    my_list.append(x)
print(my_list)
'''
