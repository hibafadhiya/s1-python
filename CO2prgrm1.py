area_square = lambda side: side ** 2
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height
side = float(input("Enter side of square: "))
print("Area of square:", area_square(side))

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("Area of rectangle:", area_rectangle(length, width))

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of triangle:", area_triangle(base, height))
