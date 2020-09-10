
# file_obj = open("filename")
# file_obj.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('/Users/jstrick/Desktop/py3intro3day/DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print()

    print("Normal:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/presidents.txt') as pres_in:
    with open('potus.txt', 'w') as pres_out:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            term, lname, fname, dob, dod, bplace, bstate, tookoffice, leftoffice, party = line.split(':')
            if party == 'Whig':
                pres_out.write(f"{fname}\t{lname}\t{party}\n")

print('-' * 60)

#  file modes: 'r' 'w' 'a' 'x'


