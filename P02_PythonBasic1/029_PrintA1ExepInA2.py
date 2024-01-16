"""

Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}



Set operations:

Find the intersection (colors in both lists): 
intersection = color_list_1.intersection(color_list_2)

Find the difference (colors in list 1 but not list 2): difference = color_list_1.difference(color_list_2)

Find the union (all unique colors from both lists): union = color_list_1.union(color_list_2)

Check if one set is a subset of the other: issubset = color_list_1.issubset(color_list_2)
D
ata manipulation:

Add or remove colors from the sets: color_list_1.add("Blue") color_list_2.remove("Green")
Convert sets to lists or other data structures: list1 = list(color_list_1) tuple2 = tuple(color_list_2)



"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

missing_colors = color_list_1.difference(color_list_2);
dupplicate_colors = color_list_1.intersection(color_list_2);

union = color_list_1.union(color_list_2)

issubset = color_list_1.issubset(color_list_2)


print(missing_colors);

print(dupplicate_colors);

print(union);
print(issubset);


from collections import Counter 
color_counts = Counter(color_list_1)
print(color_counts);

sorted_colors = sorted(color_list_1)
print(sorted_colors);