numbers = input("enter a list of integers seperated by spaces:")
numbers_list = [int(x) for x in numbers.split()]
result = ['over' if x > 100 else x for x in numbers_list]
print("modified list:",result)