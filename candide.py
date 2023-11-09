def lengh(mot) :
    if len(mot) >= 4 and len(mot) <= 25 :
        return True

def find(mot, m) :
    return mot.count(m)

word = input("enter a word : ").upper()

while lengh(word) != True :
    word = input("Enter a word with a number of letters between 4 and 25 : ")

t = []

for i in range(len(word)) :
    t.append("*")
k = 0
w = 0

while True :
    letter = input("Enter a letter : ").upper()
    if find(word , letter) == 0 :
        k += 1
    else :
        for i in range(len(word)) :
            if word[i] == letter :
                w += 1
                t[i] = letter
        print(" ".join(t))
    if k == 5 or w == len(word):
        break 

if k == 5 :
    print("Sorry, you lose !")
if w == len(word) :
    print("Congratulations, you win")

