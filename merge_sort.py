def merge_sort(a):
	l = len(a)
	if l > 1:
		mid = l // 2
		L = a[:mid]
		R = a[mid:]
		merge_sort(L)
		merge_sort(R)

		i = j = k = 0

		while  i < len(L) and j < len(R):
			if L[i] <= R[j]:
				a[k] = L[i]
				i += 1
			else:
				a[k] = R[j]
				j += 1

			k += 1

		while i < len(L):
			a[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			a[k] = R[j]
			j += 1
			k += 1

a = [5,4,6,2,1]
merge_sort(a)
print(a)


			
		 	 