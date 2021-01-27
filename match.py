#this program tells the percentage of similarity between  two words or sentences


#input 1: test
#input 2: test.txt
#output --> the resemblance percentage: 50%
phrase = input("Enter sentence or word: ").strip().lower()
target = input("Target: ").strip().lower()

target2 = []
phrase2 = []
for a in target:
    target2.append(a)

for e in phrase:
    phrase2.append(e)

count = 0

if len(phrase2) <= len(target2):
    for i in range(len(phrase2)):
        #print(phrase2[i], target2[i])
        if phrase2[i] == target2[i]:
            count += 1

    percentage = (count/len(target2))*100
elif len(target2) <= len(phrase2):
    for i in range(len(target2)):
        #print(phrase2[i], target2[i])
        if phrase2[i] == target2[i]:
            count += 1

    percentage = percentage = (count/len(phrase2))*100

"""
def percentage(num, lenght):
     return (num/lenght)*100
"""
print(f"{percentage}%")

"""
print(target2)
print(phrase2)
print(count)
print(percentage(count, len(target2)))
"""#was debugging the hard way