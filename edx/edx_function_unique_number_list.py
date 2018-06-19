# A function that accepts 2 lists and return a sorted list with
# unique common elements only.

def unique_common(a, b):
    a.sort()
    b.sort()
    output_list = []
    if len(a) >= len(b):
        x = len(a)
    else:
        x = len(b)
    while x > 0:
        overly_complicated_variable = False
        if a[0] == b[0]:
            working_int = a.pop(0)
            for items in output_list:
                if items == working_int:
                    overly_complicated_variable = True
            if not overly_complicated_variable:
                output_list.append(working_int)
            del b[0]
        else:
            if a[0] > b[0]:
                del b[0]
            elif a[0] < b[0]:
                del a[0]
        if not a:
            break
        if not b:
            break
        x -= 1
    if not output_list:
        return
    else:
        return output_list
