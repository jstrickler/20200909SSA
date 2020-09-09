
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print("""Guido's the "BDFL" of Python""")

#  \n \r \t \b \f
print(s1)
print(s2)
print(s1 == s2)
print("Finished.")

insert_statement = """
insert into CUST
(firstname, lastname, quote) values (?, ?, ?)
where CUST_ID = ?
"""
