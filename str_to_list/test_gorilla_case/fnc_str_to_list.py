def f_str_to_list( str ) :
	ll = []
	for elem in str :
		if elem != " ":
			if elem.isdigit():
				if int(elem) <= 5:
					ll.append(elem)
			else:
				ll.append(elem)
	return ll