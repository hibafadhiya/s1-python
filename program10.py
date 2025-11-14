filename = input("Enter the file name: ")
parts = filename.split('.')
if len(parts) > 1:
    print("File extension is:", parts[-1])
else:
    print("No extension found.")
