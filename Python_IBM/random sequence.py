import random

input_d = input("Введи целое положительное число искомого количества повторений: ")
while input_d.isdigit() == False:
    print("Ты ввел не целое положительное число, попробуй еще раз")
    input_d = input("Введи целое положительное число искомого количества повторений: ")

siq_length = int(input_d) #a number of the same numbers

print("Будем считать через сколько повторений выпадет " + str(siq_length) + " подряд повторений числа 0 или 1")
the_same = 0
counter = 0 #counter for the attemtps
number_1 = int

while True: 
    counter += 1
    number = random.randint(0,1)
    if not (number_1 == 0 or number_1 == 1):
        pass
        #print("number_1 does not exists")
    else:
        if number == number_1:
            #print("this is the same number as previous")
            the_same += 1
            #print("The number repeats " + str(the_same) + "raz")
        else:
            the_same = 0
            #print ("the number is not the same as previous")
    number_1 = number
    print(str(counter) + ". The number is: " + str(number))
    if the_same == siq_length-1:
        #print("now counter is 10 and we break the loop")
        print("The same number repeats " + str(the_same+1) + " times in a row and the number is: "+ str(number))
        print("we needed only " + str(counter) + " times for this")
        break
