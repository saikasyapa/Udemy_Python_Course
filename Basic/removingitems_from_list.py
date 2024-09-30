inputs = ["Monitor", "Keyboard","Mouse","CPU","Printer","Scanner"]

for number,item in enumerate(inputs):
    print(number + 1,item)
valid_choices = []
for i in range(1,len(inputs) + 1):
    valid_choices.append(str(i))


computer_parts = []
choice = " "

while True:
    choice = input("Select the items from the above list of data")
    if choice == "0":
        print(f"Iam done, you are selected items are {computer_parts}")
        break
    if choice in valid_choices:
        index = int(choice) - 1
        selected_item = inputs[index]
        if selected_item in computer_parts:
            computer_parts.remove(selected_item)
            print(f"{selected_item} is removed.")
        else:
            computer_parts.append(selected_item)
            print(f"You are selected {selected_item} and the list is {computer_parts}")
    else:
        print("Invalid Selection!, Please select from the above list")
print(computer_parts)