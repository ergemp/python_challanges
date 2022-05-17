from is_palindrome.solution1.functions import *

import django
from django.http import HttpResponse

print(django.get_version())




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")