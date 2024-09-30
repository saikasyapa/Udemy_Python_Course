# def banner_text(text):
#     screen_width = 80
#     if len(text) > screen_width - 4:
#         print("EEk!!")
#         print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
#     if text == '*':
#         print("*" * screen_width)
#     else:
#         output_string = f"**{text.center(screen_width - 4)}**"
#         print(output_string)
# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If life seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're feeling in the dumps,")
# banner_text("Don't be silly chumps,")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...")
# banner_text("*")
#
# numbers = [4,8,5,2,0,3,8]
# print(sorted(numbers))


# def banner_text(text,screen_width):
#
#     if len(text) > screen_width - 4:
#         raise ValueError (f"String {text} is larger then specified width {screen_width}")
#         # print("EEk!!")
#         # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
#     if text == '*':
#         print("*" * screen_width)
#     else:
#         output_string = f"**{text.center(screen_width - 4)}**"
#         print(output_string)
# banner_text("*",66)
# banner_text("Always look on the bright side of life...",66)
# banner_text("If life seems jolly rotten,",66)
# banner_text("There's something you've forgotten!",66)
# banner_text("And that's to laugh and smile and dance and sing,",66)
# banner_text(" ",66)
# banner_text("When you're feeling in the dumps,",66)
# banner_text("Don't be silly chumps,",66)
# banner_text("Just purse your lips and whistle - that's the thing!",66)
# banner_text("And... always look on the bright side of life...",66)
# banner_text("*",66)

# def banner_text(text,screen_width=80):
#
#     if len(text) > screen_width - 4:
#         raise ValueError(f"String {text} is larger then specified width {screen_width}")
#         # print("EEk!!")
#         # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
#     if text == '*':
#         print("*" * screen_width)
#     else:
#         output_string = f"**{text.center(screen_width - 4)}**"
#         print(output_string)
# banner_text("*")
# banner_text("Always look on the bright side of life...")
# banner_text("If life seems jolly rotten,")
# banner_text("There's something you've forgotten!")
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're feeling in the dumps,")
# banner_text("Don't be silly chumps,")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...") 
# banner_text("*")


def banner_text(text = " ",screen_width=80):                                      ## update

    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger then specified width {screen_width}")
        # print("EEk!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    if text == '*':
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)
banner_text("*",60)
banner_text("Always look on the bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(screen_width=60)                                                               ### update
banner_text("When you're feeling in the dumps,",60)
banner_text("Don't be silly chumps,",60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life...",60)
banner_text("*",60)


