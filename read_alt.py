
#  read one file, write to two other files depending on data

INPUT_FILE = 'DATA/alt.txt'
OUTPUT_FILE_A = 'a.txt'
OUTPUT_FILE_B = 'b.txt'

with open(INPUT_FILE) as alt_in:
    with open(OUTPUT_FILE_A, 'w') as a_out:
        with open(OUTPUT_FILE_B, 'w') as b_out:
            for line in alt_in:
                if line.startswith('a'):
                    a_out.write(line)
                elif line.startswith('b'):
                    b_out.write(line)

# alt_in = open(INPUT_FILE)
# # ...
# alt_in.close()
