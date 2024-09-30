# jabber = open('jabberwocky.txt','r')
#
# # for line in jabber:
# #     print(line,end="")
# #     # print(len(line))
# #
# # jabber.close()
#
# for line in jabber:
#     print(line.strip())
#     # print(len(line))
#
# jabber.close()

# ####### another method #######
# with open('jabberwocky.txt','r') as jabber:
#     for line in jabber:
#         print(line.strip())

## file reading 3 types
# 1)readlines: it display the data in list
#2) read : display exact text normally
#3) readline : read only line

# with open('jabberwocky.txt','r') as jabber:
#     lines = jabber.readlines()
# # print(lines)
# for character in reversed(lines):
#     print(character,end='')

# with open('jabberwocky.txt','r') as jabber:
#     lines = jabber.read()
# # print(lines)
# # for character in reversed(lines):    ### text reversed
# #     print(character,end='')

# with open('jabberwocky.txt','r') as jabber:
#     while True:
#         line = jabber.readline().strip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break

################### or ##########################
with open('jabberwocky.txt','r',encoding='UTF-8') as jabber:
    for item in jabber:
        print(item.rstrip())





