def shortest_path(a, begin, end):
	n_rows = len(a)
	n_cols = 0
	if n_rows == 0:
		return -1
	n_cols = len(a[0])
	# Intialize a queue with (x,y,d) where d is the distance between begin and co-ordinate (x, y)
	q = [(begin[0], begin[1], 0)]
	# make a queue of visited co-ordinates 
	visited = []
	for i,j,d in q:
		visited.append((i,j))
		# If we reach end co-ordinate, exit with distance d
		if i == end[0] and j == end[1]:
			return d
		# Look for four neighbour points of (i,j)
		for x,y in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
			# if the neighbouring point (x,y) is not visited, add to the queue if value at (x,y) = 1
			if 0 <= x < n_rows and 0 <= y < n_cols and (x,y) not in visited:
				# Append to queue if value == 1 with distance = current co-ordiatnate distance + 1
				if a[x][y] == 1:
					q.append((x,y,d+1))

	# -1 is returned for all failure cases such as array is empty or end co-ordiate is outside array
	return -1



array = [[1, 1, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 1, 0, 1, 1, 1, 0, 1, 0, 1 ],
	[1, 0, 1, 0, 1, 1, 0, 1, 1, 1 ],
	[1, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
	[0, 1, 0, 1, 1, 1, 0, 1, 1, 1 ],
	[0, 0, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
	[1, 1, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ]];

begin = (2,4)
end = (8,9)
print(shortest_path(array, begin,end))