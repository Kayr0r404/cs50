# python3

ext = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

file = input("put in your file: ")
file_ext = ""
for idx in range(len(file)):
    if file[idx] == ".":
        file_ext = file[idx:].strip().lower()
if file_ext in ext[:4]:
    if file_ext == ".jpg":
        file_ext = ".jpeg"
    print(f"image/{file_ext[1:]}")
elif file_ext == ".pdf":
    print("application/pdf")
elif file_ext == ".txt":
    print("text/plain")
elif file_ext == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
