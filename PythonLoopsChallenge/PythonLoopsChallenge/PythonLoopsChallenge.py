answer = None
list = ["Exit", "Learn Python", "Learn C++", "Go to the Gym", "Watch a movie", "Eat a meal", "Go to bed"]

while answer != "0":
    print("Please choose your option from the list below:")
    for i in range(len(list)):
        print("{}. {}".format(i, list[i]))

    answer = input("What do you choose? ")

    while not answer.isnumeric() or int(answer) > 6 :
        print("Invalid answer, try again ")
        answer = input()

    print("You chose {}, {}".format(answer, list[int(answer)]))

else:
    print("Thank you for answering, have a nice day!")

