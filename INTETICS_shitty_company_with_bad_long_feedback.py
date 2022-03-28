import math


def solver_task_1():
	print("""
	input first parameter:
	-string of size N^2, that describes square matrix of characters N*N;
	The first string is converting to matrix using the following rule. String "QWEASDZXC" forms the matrix:
	['Q','W','E',
	'A','S','D',
	'Z','X','C']
	- press Enter
	""")
	matrix_str = input().upper()
	matrix_size = len(matrix_str)
	matrix_rank = matrix_size ** 0.5
	
	# checking input data
	if not round(matrix_rank, 4) == math.ceil(matrix_rank):
		raise Exception(f"This str doesn't define square matrix, num of elements {matrix_size} is not square")
	else:
		print("""
		input second parameter:
		-string that describes given word.
		-press Enter
		And than program will find positions of required letters
		""")
		# store word for searching, upper or lower case, doesn't matter
		search_word = input().upper()
		
		# saving positions of letters in str
		positions_in_str = []
		# search each letter
		
		# current_position = 0
		for letter in search_word:
			current_position = 0
			# About PEP 8 warning about not using current_position yet:
			# if comment previous line, script will find words without returning to start each time,
			# when is searching new letter
			# that why word will be from left to right in string
			# (how we read, but without other symbols in str)
			while current_position < matrix_size:
				if matrix_str[current_position] == letter:
					positions_in_str.append(current_position)
					current_position += 1
					break
				current_position += 1
		# now we have positions in string program may transform it in columns and rows
		# (coordinates)
		coordinates = []

		for coordinates_pos, letter_pos in enumerate(positions_in_str):
			row_num = int(letter_pos // matrix_rank)
			column_num = int(letter_pos % matrix_rank)
			coordinates.append([row_num, column_num])
		if len(coordinates) == len(search_word):
			print("Answer is:")
			print(coordinates)
		else:
			print("There is no word that satisfies condition")
		# passed tests correctly:
		# QLGNAEKIRLRNGEAE kiNg
		# QLGNAEKIRLRNGEAEQLGNAEKIRLRNGEAE KIng
		# QLGNAEKIRLRNGEAEQLGNAEKIRLRNGEAEQLGNAEKIRLRNGEAEQLGNAEKIRLRNGEAE king
		# HnOlasdfjyayToRunjsdjksdasdasdas nowaytorun
		# HnOlasdfjyayToRu way
		# smfbnvwkjndvjhay way


if __name__ == "__main__":
	solver_task_1()
	