# from scipy import spatial

# dataSetI = [3, 54, 3, 2]
# dataSetII = [3, 14, 7, 2]
# result = 1 - spatial.distance.cosine(dataSetI, dataSetII)

# print(result)

import math

def takeinputs():

    q1 = "What are you interested in? \n 1) Sports \n 2) Tech \n 3) Religion \n 4) Music \n 5) Dance \n"
    q2 = "What's most important to you? \n 1) High paying job \n 2) Good friends \n 3) A nice house \n 4) Education \n 5) Having fun \n"
    q3 = "What's your GPA? \n 1) < 2 \n 2) < 2.5 \n 3) < 3 \n 4) < 3.5 \n 5) > 3.5 \n"
    q4 = "What's your major related to? \n 1) Tech \n 2) Art \n 3) Human science \n 4) Social science \n 5) Business \n"
    q5 = "Whats your cultural background? \n 1) American \n 2) Asian \n 3) African \n 4) European \n 5) South America \n"
    q6 = "HOw are you feeling? \n 1) Happy \n 2) What is life? \n 3) Annoyed \n 4) Angry \n 5) Excited \n"
    q7 = "Would do prefer to go out to a party on a saturday night or stay in the house and read a book? \n 1) Book \n 2) Party"


    print("\n\nHi! we are going to ask some questions to match you with your potential friends!")

    # person 1

    #ask for the weights

    #weights should allways be in the same order!!

    weights = [0]*7
    print("\nPlease tell us on a scale from 1-8 how important you find the following traits in a person")

    print("\nShared interests")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[0] = inp

    print("\nsimilar ambitions and goals")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[1] = inp

    print("\nintellect level")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[2] = inp


    print("\nacademic background")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[3] = inp

    print("\ncultural background")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[4] = inp

    print("\nemotional state")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[5] = inp


    print("\nintro/extro")
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>8):
        inp = int(input("Please enter a number between 1 and 8: "))
    weights[6] = inp





    #ask questions

    print("\nPlease input the the number associated the option that best describes you")
    answers = [0]*7

    print("\n"+ q1)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[0] = inp

    print("\n"+ q2)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[1] = inp

    print("\n"+ q3)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[2] = inp


    print("\n"+ q4)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[3] = inp

    print("\n"+ q5)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[4] = inp

    print("\n"+ q6)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>5):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[5] = inp

    print("\n"+ q7)
    inp = int(input("Enter your input: "))
    while (inp<1 or inp>2):
        inp = int(input("Please enter a number between 1 and 5: "))
    answers[6] = inp

    W1 = weights
    A1 = answers
    print(W1)
    print(A1)

    return (W1, A1)
    


#person 2


(W1, A1) = takeinputs()


print("\n\n\n\n\n\n\n --------PERSON 2------------")

(W2, A2) = takeinputs()


# print([1,2]*[0,0])


v1 = [0]*7
v2 = [0]*7
for i in range(7):
    v1[i] = (W1[i]) * (A2[i])

for i in range(7):
    v2[i] = (W2[i]) * (A1[i])

#do the same


#make the vectors

#compare

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sum_of_xx, sum_of_xy, sum_of_yy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sum_of_xx += x*x
        sum_of_yy += y*y
        sum_of_xy += x*y
    return (sum_of_xy)/math.sqrt((sum_of_xx)*(sum_of_yy))



print(v1, v2, cosine_similarity(v1,v2))