import random
correct_answer = random.randint(1, 101) #隨機 0 ~ 100
a = 101
answer = 101
while answer != correct_answer:
    a = input ("Enter a number: ")
    #print("type a = ",type(a))
    answer = int(a)
    if (answer < correct_answer):
        print("Too small")
    elif (answer > correct_answer):
        print("Too big")
print("Correct !")