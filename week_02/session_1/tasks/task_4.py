# Week 2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetable = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetable)
print(both)
#tomata

# Why does the following code diplay five items?

food = fruit.union(vegetable)
print(food)

# Add an item to fruit
fruit.add('bananas')
# Remove an item from vegetables
vegetable.remove('leek')
# Find and display symmetric difference of the two sets
sy=fruit.symmetric_difference(vegetable)
print(sy)