# python3

greeting = input("please greet the custome. ").strip().lower().split()

if "hello" in greeting or "hello," in greeting:
    print("$0")
elif greeting[0].startswith("h"):
    print("$20")
else:
    print("$100")
