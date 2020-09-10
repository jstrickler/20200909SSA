import sys

print(sys.argv)

for file_name in sys.argv[1:]:  # process all words on the command line
    print("processing", file_name)
    with open(file_name) as file_in:
        pass

