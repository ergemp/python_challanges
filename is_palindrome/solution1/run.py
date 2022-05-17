from is_palindrome.solution1.functions import *

str = "otto"

if (str == list_to_str(f_reverse(str))):
    print ('is palindrome')
else:
    print ('is not palindrome')