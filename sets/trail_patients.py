# trail_1 = {"Bob","Charley","Georgia","John"}
# trail_2 = {"Anne","Charley","Eddie","Georgia"}
#
# check_set = trail_1.intersection(trail_2)
# print(check_set)
#
# farm_animals = {"sheep","hen","cow","horse","goat"}
# wild_animals = {"lion","elephant","tiger","goat","panther","horse"}
# potential_rides = {"horse","camel","donkey"}
#
# # mounts = farm_animals.intersection(wild_animals,potential_rides)
# mounts = farm_animals & wild_animals & potential_rides
# print(mounts)

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

a = text.split()
b =set(a)
prep_used = prepositions.intersection(b)
print(prep_used)