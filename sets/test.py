scorpions = {"emperor",'red claw','arizona','forest','fat tail'}
snakes = {"python",'cobra','viper','anaconda','mamba'}
spiders = {'tarantula','black widow','wolf spider','crab spider'}
vespas = {'yellowjacket','hornet','paper wasp'}

bite = snakes.union(spiders)
print(bite)
snakes.update(spiders)           #################### update will update in the existing set don't create a new set
print(snakes)

# Key Differences:
# union() creates a new set without modifying the original sets.
# update() modifies the original set it's called on.

sting = scorpions.union(vespas)
print(sting)
all = snakes.union(spiders,scorpions,vespas)
print(all)