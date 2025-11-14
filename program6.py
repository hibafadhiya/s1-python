

text = input("enter a string:")
result = text[0] + text[1:].replace(text[0], '$')
print("modified string" , result)