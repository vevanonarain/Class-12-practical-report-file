#Task 28 - 27/6/2023
#Vevan O Narain S7-C

"""Write a menu based program to perform the following task on a Python tuple WORDS.
A sample tuple WORDS = ('LAN', 'MAN', 'WAN', 'VoIP', 'HTTPS')
The tasks are:
i) Add a new word in the tuple WORDS, entered by the user
ii) Display all words stored in the tuple WORDS
iii) Sort the tuple WORDS alphabetically"""

words = ('LAN', 'MAN', 'WAN', 'VoIP', 'HTTPS')

new = 23
words = words + (new, )

print(words)

x = (sorted(words))

print(x)