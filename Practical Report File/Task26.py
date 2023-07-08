#Task 26 - 27/6/2023
#Vevan O Narain S7-C

"""Create a Tuple SENTENCES of 5 sentences entered by the users and display the followings:
All words starts with A or a and size more than 4 characters
All words ends with A or a and size less than 4 characters
All sentences starts with alphabets A or a"""

sentences = ()
sentences_l = list(sentences)
a = ()

for i in range(5):
    sentence = input("Enter Sentence: ")
    sentences_l.append(sentence)

a_sent = ()

for i in sentences_l:
    x = i.split()

    if i[0].lower() == "a":
        a = a + (i, )

    for j in range(len(x)):
        if x[j][0].lower() == "a":
            a_sent = a_sent + (x[j],)

a_sent_large = ()
a_sent_small = ()

for i in a_sent:
    if len(i) > 4:
        a_sent_large = a_sent_large + (i, )
    else:
        a_sent_small = a_sent_small + (i, )

print(f"Words which start with 'A' or 'a' and are more than 4 characters are {a_sent_large}")
print(f"Words which start with 'A' or 'a' and are less than 4 characters are {a_sent_small}")
print(f"Sentences which start with 'A' or 'a' are {a}")