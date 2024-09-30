animals = {'turtle','horse','robin','python','swallow','hedgehog','wren','aardvark','cat'}
birds = {'robin','swallow','wren'}

print(f"birds is a subset of animals : {birds.issubset(animals)}")
print(f"animals are superset of birds : {animals.issuperset(birds)}")

print(40 * "*" ,"Negative test" ,40 * "*")

print(f"birds is a subset of animals : {animals.issubset(birds)}")
print(f"animals are superset of birds : {birds.issuperset(animals)}")

print(birds <= animals)
print(birds < animals)
print(animals > birds)
print(animals >= birds)
print(40 * "*")
garden_birds = {'robin','swallow','wren'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds > birds)
print(40 * "*")
more_birds = {'budgie','swallow','wren'}
print(more_birds <= garden_birds)
