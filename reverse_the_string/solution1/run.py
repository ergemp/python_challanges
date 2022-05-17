from reverse_the_string.solution1.f_reverse import f_reverse
from reverse_the_string.solution1.f_reverse import list_to_str

str1 = 'otto'
str2 = 'loko'

ll = []

for i in range(len(str2)):
    #print (str2[len(str2)-1-i])
    ll.append(str2[len(str2)-1-i])

#print(ll)


print(list_to_str(f_reverse(str1)))
