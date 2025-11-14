k=[-2,-1,0,1,2,3]
pos_list=[x for x in k if x>0]
print("pos num:", pos_list)

n= 10
squares = [x**2 for x in range(1,n+1)]
print("Square:",squares)

word="hello"
vowels=[ch for ch in word if ch in 'aeiou']
print("vowels in word:", vowels)

word2 = "cat"
ordinals = [ord(ch) for ch in word2]

print("ordinal values:", ordinals)
