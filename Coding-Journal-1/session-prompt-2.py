def add_float():
	x = 5.7
	y = 7.5
	z = x + y
	print(z)
	print(type(z))

def subtract_int():
	x = 18
	y = 11
	z = x - y
	print(z)
	print(type(z))

def product_int_float():
	x = 12
	y = 7.2
	z = x * y
	print(z)
	print(type(z))

def main():
	add_float()
	subtract_int()
	product_int_float()

if __name__ == "__main__":
	main()