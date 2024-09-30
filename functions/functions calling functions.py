def is_palindrom(string):
    backwards = string[::-1]
    return backwards == string
# # print(is_palindrom('rotator'))
# word = input("Enter your palindrom word")
# if is_palindrom(word):
#     print(f"given word {word} is a palindrom")
# else:
#     print(f"given word {word} is not a palindrom")

def palindrome_sentence(sentence):
    """
    This function is used to check whether the given
    string is palindrome or not
    :param sentence: The input data to check the string
    :return: Return we get whether the given string is palindrome or not
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string = string + char
    print(string)
    return is_palindrom(string)

word = input("Enter your palindrom word")
if palindrome_sentence(word):
    print(f"given word '{word}' is a palindrom")
else:
    print(f"given word {word} is not a palindrom")