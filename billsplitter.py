# Made following a tutorial from JetBrains Academy
# Made by Luke T.

import random


def friend_count():
    num_friends = input("Enter the number of friends joining (including you): \n")

    while num_friends.isnumeric():
        int_num_friends = int(num_friends)

        if int_num_friends > 0:
            friend_dict(int_num_friends)
        else:
            print("No one is joining for the party")
            exit()

    while not num_friends.isnumeric():
        print("No one is joining for the party")
        exit()


def friend_dict(numKeys):
    print("Enter the name of every friend (including you), each on a new line.")
    friends = {}

    for friend in range(numKeys):
        key = input()
        amount = 0
        friends[key] = amount

    # print(friends)
    bill_pay(friends)


def bill_pay(friends):
    bill = float(input("Enter the total bill value: \n"))
    each_owes = bill / len(friends)
    split_bill = dict()

    # Initialize values for Friends Dictionary with equal portions
    for friend in friends:
        friends[friend] = each_owes

    lucky = input('Do you want to use the "Who is Lucky" feature? (Y/N) \n').capitalize()

    # Lucky Logic Gate
    if lucky[0] == "N":
        print("No one is going to be lucky")

    elif lucky[0] == "Y":
        lucky_one = random.choice(list(friends.keys()))
        print("{} is the lucky one!".format(lucky_one))

        # Distributes lucky friend's portion to the other friends.
        for friend in friends:
            if friend is not lucky_one:
                friends[friend] += each_owes / (len(friends) - 1)
                split_bill[friend] = round(friends[friend], 2)
            else:
                friends[friend] = 0.00

    else:
        print("Sorry, that is not a valid response. Please try again.")
        bill_pay(friends)

    # Rounding Loop (Done at end to prevent rounding error)
    for friend in friends:
        split_bill[friend] = round(friends[friend], 2)

    print(split_bill)
    exit()


if __name__ == "__main__":
    friend_count()
