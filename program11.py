colors = input("Enter the color names separated by commas: ")
color_list = [color.strip() for color in colors.split(",")]

print("First color:", color_list[0])
print("Last color:", color_list[-1])

