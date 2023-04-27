#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""


from typing import runtime_checkable


people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)

Choose_a_person = input("Choose a person from the list to replace: ")
replacement = input("Enter the replacement: ")

if Choose_a_person in people:
    index = people.index(Choose_a_person)
    people[index] = replacement
    print(people)
