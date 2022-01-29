from api import fetcher

def main_wrapper():
	# project start
	print(f"function name: {main_wrapper.__name__}")

	fetcher.states_accessor()
# project end

if __name__ == "__main__":
	main_wrapper()