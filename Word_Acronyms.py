phrase = input("Please enter a phrase: ")
acc = (phrase.split())
print(acc)
fin = ""
for word in acc:
    if word not in ["is"Depa, "and"]:
        fin += word[0].upper()

print(fin)