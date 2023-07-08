#Task 07 - 23/6/2023
#Vevan O Narain S7-C 

"""Define a function to input an amount of money and display MINIMUM CURRENCY NOTES (out of
2000/500/200/100/50/20/10/5/2/1) required to have that money."""

def countCurrency(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notesCount = {}

    for note in notes:
        if (amount >= note):
            notesCount[note] = amount // note
            amount %= note

    print("Currency count: ")

    for key, val in notesCount.items():
        print(f"{key}: {val}")


amount = int(input("Enter the amount: "))
countCurrency(amount)