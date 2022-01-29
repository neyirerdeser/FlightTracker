from api import utils

def main_wrapper():
	# project start
	print(f"function name: {main_wrapper.__name__}")
	utils.solid_example_1(example_param_1="A", example_param_2=3)
	utils.solid_example_2(5)
	utils.solid_exmaple_3() # float = 4.3
	utils.solid_exmaple_3(2.7) # float = 2.7
# project end

if __name__ == "__main__":
	main_wrapper()