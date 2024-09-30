# def center_text(text, file=None):###################text = parameter
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     output = " " * left_margin + text
#
#     if file:
#         print(output,file=file)
#         print(output)
#
# with open('aaa.txt','w',encoding='utf-8') as files:
#     center_text("spam and eggs", files)
#     center_text("spam,spam and eggs", files)
#     center_text("spam,spam,spam and eggs", files)
#     center_text(201, files)
#     center_text(200000001, files)
#
#
# center_text("spam and eggs")####################### inside the function is 'Argument'
# center_text("spam,spam and eggs")
# center_text("spam,spam,spam and eggs")
# center_text(str(201))
# center_text(200000001)

########################### or ################################

def center_text(text, file=None):###################text = parameter
    text = str(text)
    left_margin = (80 - len(text)) // 2
    output = " " * left_margin + text
    print(output,file=file)
with open('aaa.txt','w',encoding='utf-8') as files:
    center_text("spam and eggs", file = files)
    center_text("spam,spam and eggs", file = files)
    center_text("spam,spam,spam and eggs", file = files)
    center_text(201, file = files)
    center_text(200000001, file = files)





