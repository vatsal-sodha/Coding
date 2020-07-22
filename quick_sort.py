def quick_sort(arr, l, r):
	if (l < r):
		q = partition(arr, l, r)
		quick_sort(arr, l, q-1)
		quick_sort(arr, q+1, r)

def partition(arr, l, r):
	i = l - 1
	x = arr[r]
	for j in range(l, r):
		if arr[j] < x:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[r] = arr[r], arr[i+1]

	return (i + 1)
arr = [5,4,6,2,1]
n = len(arr)
quick_sort(arr,0,n-1)
print(arr)