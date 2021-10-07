filename = 'data/alice.txt'
'''with open(filename, encoding='utf-8') as f:
contents = f.read()'''


try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")