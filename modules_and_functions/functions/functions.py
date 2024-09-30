# def python_food():
#     print("Small snakes and rats")
#
# python_food())

# def center_text(text):###################text = parameter
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)
# center_text("spam and eggs")####################### inside the function is 'Argument'
# center_text("spam,spam and eggs")
# center_text("spam,spam,spam and eggs")
# center_text(str(201))
# center_text(200000001)

########### in this below data we are using *args to print data with spaces for last example #################

# def center_text(*args, sep = ' ', end = '\n', file = None, flush = None):
#     text = ""
#     for arg in args:
#         text = text + str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text,end=end, file=file, flush=flush)
# center_text("spam and eggs")
# center_text("spam,spam and eggs")
# center_text("spam,spam,spam and eggs")
# center_text(str(201))
# center_text(200000001)
# center_text("first",'second',3,4,"five",sep=":")


# def center_text(*args, sep = ' ', end_char = '\n', centered_file = None, flush_me = False):
#     text = ""
#     for arg in args:
#         text = text + str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text,end=end_char, file=centered_file, flush=flush_me)
# center_text("spam and eggs")
# center_text("spam,spam and eggs")
# center_text("spam,spam,spam and eggs")
# center_text(str(201))
# center_text(200000001)
# center_text("first",'second',3,4,"five",sep=":")

#################### Creating a function that allows text to be printed as file #######################

# def center_text(*args, sep = ' ', end_char = '\n', centered_file = None, flush_me = False):
#     text = ""
#     for arg in args:
#         text = text + str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text,end=end_char, file=centered_file, flush=flush_me)
#
# with open("textfile.txt",'w',encoding='utf-8') as textfile:
#     center_text("spam and eggs",centered_file = textfile)
#     center_text("spam,spam and eggs",centered_file = textfile)
#     center_text("spam,spam,spam and eggs",centered_file = textfile)
#     center_text(str(201),centered_file = textfile)
#     center_text(200000001,centered_file = textfile)
#     center_text("first",'second',3,4,"five",sep=":",centered_file = textfile)


#################### Another method to Creating a function that allows text to be printed as file #######################
def center_text(*args, sep = ' '):
    text = ""
    for arg in args:
        text = text + str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

with open('new_textfile.txt','w',encoding='utf-8') as new_textfile:
    s1 = center_text("spam and eggs")
    print(s1)
    print(s1, file=new_textfile)
    s2 = center_text("spam,spam and eggs")
    print(s2)
    print(s2, file=new_textfile)
    s3 = center_text("spam,spam,spam and eggs")
    print(s3)
    print(s3, file=new_textfile)
    s4 = center_text(201)
    print(s4)
    print(s4, file=new_textfile)
    s5 = center_text(200000001)
    print(s5)
    print(s5, file=new_textfile)
    s6 = center_text("first",'second',3,4,"five",sep=":")
    print(s6)
    print(s6, file=new_textfile)