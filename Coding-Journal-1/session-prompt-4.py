class favorite_animal:
	def __init__(self,length_arm=float,length_leg=float,num_eye=int,tail=bool,furry=bool):
		self.length_arm = length_arm
		self.length_leg	= length_leg
		self.num_eye = num_eye
		self.tail = tail
		self.furry = furry

	def print_animal(self):
		print(f"Arm Length = {self.length_arm}")
		print(f"Leg Length = {self.length_leg}")
		print(f"Number of eyes = {self.num_eye}")
		print(f"Has tail = {self.tail}")
		print(f"Is furry = {self.furry}")

def main():
	my_fav_animal = favorite_animal(6.9, 4.2, 0, False, True)
	my_fav_animal.print_animal()

if __name__ == "__main__":
	main()