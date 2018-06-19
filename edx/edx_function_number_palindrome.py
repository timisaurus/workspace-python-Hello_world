# Accepts a list containing numbers as parameter and checks wether
# its a palindrome or not.

def crazy_list(some_list):
    compare_list_a = []
    compare_list_b = []
    for items in some_list:
        compare_list_a.append(some_list.pop(0))
        compare_list_b.append(some_list.pop(-1))
    while len(compare_list_a) > 0:
        if compare_list_a[0] == compare_list_b[0]:
            del (compare_list_a[0])
            del (compare_list_b[0])
            if len(compare_list_a) == 0:
                return True
        else:
            return False
