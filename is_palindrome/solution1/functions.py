def f_reverse(str):
    ll = []
    for i in (range(len(str))):
        ll.append(str[len(str)-1-i])
    return ll

def list_to_str(ll):
    str = ''
    for elem in ll:
        str += elem
    return str