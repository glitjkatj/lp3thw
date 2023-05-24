formatter = "{} {} {} {}"

print(formatter.format("uno", "dos", "tres", "quatro"))
print(formatter.format(1, 2, 3, 4))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Some dude",
    "Wrote a poem",
    "About a red wheelbarrow",
    "That I had to read in school"
))
