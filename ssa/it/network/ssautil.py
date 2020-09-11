def main():
    print("In module")
    spam()
    toast()
    toast()
    toast()

def spam():
    print("Hello from spam()")
    _ham()

def _ham():  # "private"
    print("    ham() ham() ham()")

def toast():
    print("Hello from toast()")

# print("My name is", __name__)

if __name__ == '__main__':
    main()
