def shortest_path(a, begin, end):
	# start_x = begin[0]
	# start_y = begin[1]
	# end_x = end[0]
	# end_y = end[1]
	# l = len(a)
	n_rows = len(a)
	n_cols = 0
	if n_rows == 0:
		return -1
	n_cols = len(a[0])
	q = [(begin[0], begin[1], 0)]
	visited = []
	for i,j,d in q:
		visited.append((i,j))
		if i == end[0] and j == end[1]:
			return d
		for x,y in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
			if 0 <= x < n_rows and 0 <= y < n_cols and (x,y) not in visited:
				if a[x][y] == 1:
					# print(x,y)
					q.append((x,y,d+1))
	return -1


# a = [[0, 1, 0, 1],
# 	 [0,1, 1, 0],
# 	 [0,0,1, 1]]
# a = [[0],
# 	[0],
# 	[0],
# 	[0]]
# print(shortest_path(a, (0,1), (0,3)))
a = [[1, 1, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 1, 0, 1, 1, 1, 0, 1, 0, 1 ],
	[1, 0, 1, 0, 1, 1, 0, 1, 1, 1 ],
	[1, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
	[0, 1, 0, 1, 1, 1, 0, 1, 1, 1 ],
	[0, 0, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
	[1, 1, 1, 0, 1, 1, 1, 1, 0, 1 ],
	[1, 0, 0, 1, 0, 0, 0, 0, 1, 1 ]];
# print(a[8][9])
# a[2][0]
print(shortest_path(a, (2,4),(8,9)))