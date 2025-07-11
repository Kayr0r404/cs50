

input = input('Put something here. ')

new_input = ""
for char in input:
    if char == " ":
        new_input += "..."
    else:
        new_input += char

print(new_input)

