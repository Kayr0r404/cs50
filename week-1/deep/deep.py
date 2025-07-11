answer = input(
    "what is the answer to the Great Question of Life, the Universe and Everything? "
).lower()

if answer.strip() in ("forty-two", "forty two", "42"):
    print("Yes")
else:
    print("No")
