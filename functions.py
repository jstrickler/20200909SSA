
def get_message():
    return "Hello SSA world"

m = get_message()
print(m)

print(get_message())

print(get_message)

def say_hello():
    message = get_message()
    print(message)

say_hello()
print()


def say(greeting):
    print("{}, world".format(greeting))

#  say(<argument>)
say("hello")
say("'sup")
say("Greetings")
print()

colors = ['red', 'purple', 'teal']

def add_color(x):
    x.append('pink')

print(colors)
add_color(colors)
print(colors)


def search_file(file_name, search_term, ignore_case=False):
    found = []
    if ignore_case:
        search_term = search_term.lower()
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            if ignore_case:
                raw_line = raw_line.lower()
            if search_term in raw_line:
                found.append((file_name, line))
    return found

results = search_file('DATA/alice.txt', 'lizard', True)

print(results, '\n')



def search_files(search_term, *file_names):
    found = []
    for file_name in file_names:
        found.extend(search_file(file_name, search_term))
    return found

results = search_files('bird', 'DATA/parrot.txt', 'DATA/alice.txt', 'DATA/words.txt')
print(len(results))
print(results)


def more_search(*file_names, search_term, ignore_case):
    found = []
    for file_name in file_names:
        found.extend(search_file(file_name, search_term, ignore_case))
    return found

print(more_search('DATA/alice.txt', 'DATA/parrot.txt', search_term='bird', ignore_case=False))
print()

def config(**values):
    print(values)

config(file_name="foo.txt", user_name="obiwan", color='pink')

print('-' * 60)




