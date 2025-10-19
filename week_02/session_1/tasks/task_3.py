# Week 2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
index_ba=fruit.index('banana')
print(fruit[index_ba])
# Display how many times "cherry" occurs
from collections import Counter
count=Counter(fruit)
print(count['cherry'])
# Unpack tuple
a,b,c=fruit
print(a,b,c)