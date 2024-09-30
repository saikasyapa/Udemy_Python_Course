# same word written in reverse also
# def is_palindrom(string):
#     backwards = string[::-1]
#     return backwards == string
# # print(is_palindrom('rotator'))
# word = input("Enter your palindrom word")
# if is_palindrom(word):
#     print(f"given word {word} is a palindrom")
# else:
#     print(f"given word {word} is not a palindrom")
############ to minimize capital small issue we use casefold
# def is_palindrom(string):
#     backwards = string[::-1]
#     return backwards.casefold() == string.casefold()
# # print(is_palindrom('rotator'))
# word = input("Enter your palindrom word")
# if is_palindrom(word):
#     print(f"given word {word} is a palindrom")
# else:
#     print(f"given word {word} is not a palindrom")


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string = string + char
    print(string)
    return string[::-1].casefold() == string.casefold()

word = input("Enter your palindrom word")
if palindrome_sentence(word):
    print(f"given word '{word}' is a palindrom")
else:
    print(f"given word {word} is not a palindrom")