#TASK ON LIST
#1.Write a program to sort a list of integers in ascending order.
list1=[1,5,7,9,8,3,4,6]
list1.sort()
print(list1)

#2.Write a program to find the maximum value in a list of integers.
a=max(list1)
print(a)

#3.Write a program to find the average of a list of numbers.
b=sum(list1)/8
print(b)

#4.Write a program to find remove all the duplicates from a list.
list2=[1,5,7,9,8,3,4,6,7,5]
c=set(list2)
print(c)
#5.Write a program to find the second smallest element in a list.
list3=[1,5,7,9,8,3,4,6]
list3.sort()
print(list3[1])

#6.Write a program to reverse a list on integers.
list3.reverse()
print(list3)

#7.Write a program to find the sum of all the elements in a list.
d=sum(list3)
print(d)
#8.Write a program to find the median of a list of numbers.
e=len(list3)/2
print(e)

### Task On Set
# 1. Create an empty set called empty set.
set1={}
print(set1)
# 2. Create a set prime numbers with values: 2, 3, 5, 7, 11.
set2={2,3,5,7,11}
print(set2)
# 3. Add 13 and 17 to the prime_numbers set.
set3={13,17}
set2.update(set3)
# 4. Create another set even_numbers with values: 2, 4, 6, 8, 10.

# 5. Find and print the intersection of prime_numbers and even_numbers.

# 6. Find and print the union of prime_numbers and even_numbers.

# 7. Find and print the difference of prime_numbers and even_numbers.

# 8. Remove 4 from the even_numbers set.

# 9. Check if 7 is present in the prime_numbers set and print the result.