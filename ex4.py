# I decided to make this about ufos instead
# I mean, why wouldn't aliens have a transportation corp?
ufos = 100
space_in_a_ufo = 4.0
pilots = 30
crew = 90
ufos_not_piloted = ufos - pilots
ufos_piloted = pilots
ufopool_capacity = ufos_piloted * space_in_a_ufo
average_crew_per_ufo = crew / ufos_piloted

print("There are ", ufos, " ufos available")
print("There are only ", pilots, " pilots available")
print("There will be ", ufos_not_piloted, " empty ufos today")
print("We can transport ", ufopool_capacity, " crews today")
print("We have ", crew, " to transport today")

# For the next line, I'm gonna leave out the spacebar between the quotes to see what happens
print("We need to put about", average_crew_per_ufo, "in each ufo")