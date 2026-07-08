names = [
    "pencil case",
    "people call me larry",
    "lily",
    "caramel",
    "afghanistan",
    "pencil-case",
    "lemon",
    "daffodil",
    "grover b shuttley",
    "roman",
]
roster = [name for name in names]
print(roster)
roster = [name.capitalize() for name in names]
print(roster)
roster = [name.split() for name in names]
print(roster)
roster = [" ".join(name.split()) for name in names]
print(roster)
roster = [" ".join([part.capitalize() for part in name.split()]) for name in names]
print(roster)
