######### int
# def fibonacci(n: int) -> int:
#     """ Return the `n` th Fibonacci number, for positive `n` ."""
#     a = 0
#     b = 1
#     if n<0:
#         print("Incorrect Input")
#     elif n == 0:
#         return a
#     elif n ==1:
#         return b
#     else:
#         for i in range(2,n + 1):
#             c = a + b
#             a = b
#             b = c
#             print(f"fibonacci series for {i} is {c}")
#         return c
#
# print(fibonacci(36))

######## string
def palindrome_sentence(sentence : str) -> str:
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

############## multiple

# def multiply(a: float,b: float) -> float:   ## a,b are parameters
#     """
#     This function is used to multiply two number
#     :param a: The firstinteger to multiply
#     :param b: the numberr to muliply with `x`
#     :return: The product of `x` and `y`
#     """
#     return a *b
#
# print(multiply(10,20)) #### 10,20 are arguments
#
# for val in range(1,11):
#     print(multiply(2 ,val))