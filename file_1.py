name = []
with open("name.txt") as file:
    for line in file:
        name.append(line.rstrip())
    
for names in sorted(name, reverse = True):
    print(f"hello, {names}")