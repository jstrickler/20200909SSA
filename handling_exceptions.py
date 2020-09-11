
FILE_NAME = 'wombats.txt'

try:
    with open(FILE_NAME) as file_in:
        pass
except (FileNotFoundError, PermissionError) as err:
    print(err, type(err))


stuff = ['tractor', 'bean', 'platypus']
try:
    print(stuff[5])
except IndexError as err:
    print(err)

values = 5.0, 3.1, 0.0, 9.2, 7.8, "6.4", 2.2, 4.9

for v in values:
    try:
        result = 23 / v
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print("finally")

    print("ALL DONE")

print("End of program.")
