  
my_dict = {
    'first_name': 'Xiu',
    'last_name': 'Zherebetska',
    'email': 'oxana1986@ukr.net',
    'age': 31
}
my_dict_values = dict.values(my_dict)
d = list(my_dict_values)
print(d)

new = []
for l in d:
    if isinstance(l, str) and len(l) > 5 and 'a' in l or isinstance(l, int) and l in range(25,40):
        new.append(l)
    print(new)

new_one = ['Xiu', 'Grey_eyes', 'Awfull_caracter']
for v in new:
    if isinstance(v, str) and 'n' not in v and 'm' not in v:
        new_one.append(v)
    print(new_one)

new_two = sorted(new_one, reverse=True)
print(new_two)

new_three = ','.join(new_two)
print(new_three)

last_one = new_three.split(',')
print(last_one)






   
        


