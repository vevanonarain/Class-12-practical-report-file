#Task 09 - 23/6/2023
#Vevan O Narain S7-C 

"""Define a function CountWord(S, W) to count and return number of occurrences of the word W
in the sentence S.
Create a List SENTENCES of 5 sentences entered by the users. Using the defined function,
count total number of occurrences of the word ‘Modern’ in the 5 sentence stored in SENTENCES."""

def countWord(s, w):
    n = 0
    x = s.split()

    for i in x:
        if i.lower() == w.lower():
            n += 1

    return n

sentences = []
modern = []

for i in range(5):
    sentence = input("Enter Sentence: ")
    sentences.append(sentence)

for j in sentences:
    modern.append(countWord(j, "Modern"))

print(sum(modern))