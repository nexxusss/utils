#this program tells the percentage of similarity between  two words or sentences


#input 1: test
#input 2: test.txt
#output --> the resemblance percentage: 50%

def take_input():
    global input_word
    global target_list
    global input_list
    
    input_word = input("Enter sentence or word: ").strip().lower()
    target = input("Target: ").strip().lower()


    target_list = []
    input_list = []
    for a in target:
        target_list.append(a)

    for e in input_word:
        input_list.append(e)

    return (input_list, target_list, input_word)


def res_perc(phrase, trgt):
    count = 0

    if len(phrase) <= len(trgt):
        for i in range(len(phrase)):
            if phrase[i] == trgt[i]:
                count += 1

        percentage = (count/len(trgt))*100
    elif len(trgt) <= len(phrase):
        for i in range(len(trgt)):
            #print(phrase2[i], target2[i])
            if phrase[i] == trgt[i]:
                count += 1

        percentage =(count/len(phrase))*100

    return percentage


if __name__ == '__main__':
    take_input()
    print(res_perc(input_list, target_list))

