color_list_1 = input("Enter first list of colors (comma separated): ").split(",")
color_list_2 = input("Enter second list of colors (comma separated): ").split(",")
color_list_1 = [color.strip() for color in color_list_1]
color_list_2 = [color.strip() for color in color_list_2]
unique_colors = [color for color in color_list_1 if color not in color_list_2]
print("Colors in list1 but not in list2:", unique_colors)

