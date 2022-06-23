#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints the fraction of amount of plurals are in the nouns
#the user inputs

nouns = input("Enter nouns: ")

myArray = nouns.split(" ")


wordCount = 0
pluralCount = 0

for i in myArray:
    wordCount = len(myArray)
    if (i[-1] == "s"):
        pluralCount += 1

    fraction = (pluralCount / wordCount) 

print("Number of words: ", wordCount)
print("Fraction of your list that is plural is", fraction)

    

    


