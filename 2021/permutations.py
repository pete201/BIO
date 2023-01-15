'''get permutations of a string'''

my_string = 'ABCD'
my_list = []
for each in my_string:
    my_list.append(each)

def permutations(in_list):
    '''input a list, output a list of permtation strings'''

    out_list = []
    # each permutation is a trunk plus permutations of the remainder until remainder has only one char
    for each in in_list:
        print(f'starting with {in_list}')
        if len(in_list) > 1:
            in_list.remove(each)
            out_list.append(each)
            print(f'remove {each} leaves {in_list}')
            out_list.append(permutations(in_list))
        else:
            out_list.append(each)

    return out_list

print(permutations(my_list))
