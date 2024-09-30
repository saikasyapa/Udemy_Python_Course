pangram = "The quick fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3,4.5,8.8,9.1,0.5,-10.2]
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)
print(missing_letter)

names= ['Graham','David','Becham','curry','Jordan','Kobe']
names.sort(key=str.casefold,reverse=True)
print(names)