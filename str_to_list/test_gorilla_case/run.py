from str_to_list.test_gorilla_case.fnc_str_to_list import f_str_to_list

str = '6 my string'

ret = f_str_to_list(str)
print(ret)

ll = []

for elem in str:
    if elem != " ":
        if elem.isdigit():
            if int(elem) <= 5:
                ll.append(elem)
        else:
            ll.append(elem)

print (ll)

