print("Please choose below items")
print("1:\tDosa")
print("2:\tIdly")
print("3:\twada")
print("4:\tpoori")
print("5:\tupma")
print("0:\tchapathi")

while True:
    choice = int(input())
    if choice == 0:
        print("iam full")
    elif choice in "12345":
        print("good")
    else:
        print("Please choose below items")
        print("1:\tDosa")
        print("2:\tIdly")
        print("3:\twada")
        print("4:\tpoori")
        print("5:\tupma")
        print("0:\tchapathi")
    choice = input()

