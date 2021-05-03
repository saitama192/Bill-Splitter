# write your code here
from random import randint


def main():
    number_of_people = 0
    people_names = []
    counter = 0
    print('Enter the number of friends joining (including you):')
    try:
        number_of_people = int(input())
    except ValueError:
        print('Invalid input')
        exit()

    if number_of_people <= 0:
        print('No one is joining for the party')
        exit()

    print('Enter the name of every fried (including you), each on a new line:')
    while counter < number_of_people:
        name = str(input())
        people_names.append(name)
        counter += 1
    d_people_names = dict.fromkeys(people_names, 0)
    d_people_names = split_bill(d_people_names)  # calling function to return the split bill value
    print(d_people_names)

def split_bill(d_people_names):
    try:
        print('Enter the total bill value:')
        b = int(input())
        c = round(b / len(d_people_names), 2)
    except ValueError:
        print('Invalid input')
    else:
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')  # logic for lucky guy starts
        ans = input()
        if ans == 'Yes':
            val = round(b / (len(d_people_names) - 1), 2)
            names = list(d_people_names.keys())
            lucky = randint(0, len(names)-1)
            lucky_name = names[lucky]
            print('{} is the lucky one!'.format(lucky_name))
            for a in d_people_names:
                d_people_names[a] = val
            d_people_names[lucky_name] = 0
            return d_people_names
        elif ans == 'No':
            print('No one is going to be lucky')
            for a in d_people_names:
                d_people_names[a] = c
            return d_people_names
        else:
            print('Invalid input')
            exit()


main()
