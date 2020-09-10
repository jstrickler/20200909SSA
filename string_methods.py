actor = "Chris Hemsworth"

print(actor)

a = actor.upper()
print(a)

print(actor.upper())

s = "monty python"
print(s.capitalize(), s.title())

print(actor.count('h'))
print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

print("Hem" in actor)
print("Haw" in actor)

s = "    monty python    "
print(s.split())

t = ":this:is::a:test:"
print(t.split(':'))

x1 = "     All my exes live in Texas    "
print("|" + x1.lstrip() + "|")
print("|" + x1.rstrip() + "|")
print("|" + x1.strip() + "|")
print()

x2 = "xyxxyyxxxyyyyxyxyAll my exes live in Texasxxxxxxxxxxyyyyyyyyyyyyyyyyyy"
print("|" + x2.lstrip('xy') + "|")
print("|" + x2.rstrip('xy') + "|")
print("|" + x2.strip('xy') + "|")
print()





