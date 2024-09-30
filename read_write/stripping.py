filename = 'jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

# chars = "' Twasebv"   #### in this it checks the bothsides and based on given letters it removes it it found the letter not in this it stops even spaces also
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

# for character in first:
#     if character in chars:
#         print(f"removing '{character}'")
#     else:
#         break

# print(80 * '*')
#
# for character in reversed(first):
#     if character in chars:
#         print(f"removing '{character}'")
#     else:
#         break
#
# print(80 * '*')


############# using removeprefix and removesuffix ##################
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
# toves_removed = first.removesuffix('toves')
# print(toves_removed)

########### creating functions for removeprefix and removesufix ###########

def pre_remove(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]
twas_removed = pre_remove(first,"'Twas")
print(twas_removed)

def suf_remove(string, suffix):
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]
toves_removed = suf_remove(first,"toves")
print(toves_removed)