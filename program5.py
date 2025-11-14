names = ["ANU","ASHARA","RAHUL","HIBA","GOPI","ARYA"]
count_a = sum(name.lower().count('a')for name in names)
print("total occurence of a",count_a)