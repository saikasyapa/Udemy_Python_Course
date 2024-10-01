a_string = "this is \na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is \na string split\t\tand tabbed"
print(raw_string)

b_string = "this is " + chr(10) + "a string split" + chr(9) + chr(9) +"and tabbed"
print(b_string)

backslash_string = "this is backslash\followed by some text"
print(backslash_string)

backslash_string_mod = "this is backslash\\followed by some text"
print(backslash_string_mod)

# error_string = r"this string ends with \"
correct_string = r"this string ends with \\" # to end the string with backslash