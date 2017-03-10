#!/usr/bin/env python

"""
Практическая задача на структуры данных: нужно провести симуляцию плей-офф чемпионата.
На входе есть список команд. Его вы задаете сами любым удобным способом. Далее вы случайным образом
(модуль random) разбиваете команды по парам и формируете сетку плей-офф - думаю все знают,
как проводятся такие турниры (1/8-я, 1/4-я, полуфиналы и финал).
Далее проводите матчи - счет определяется случайным образом. По окончании турнира нужно иметь
возможность запросить и посмотреть как выступила в турнире та или иная команда - с
кем на какой стадии играла, счет матча.
"""

import random


def _read_file_to_list(file_name):
    with open(file_name) as f:
        team_list = [line.rstrip('\n') for line in f]
    f.close()
    return team_list

list_of_teams = _read_file_to_list('epl_list')
l_teams = list_of_teams[:]
teams = {}
for i in list_of_teams:
    teams[i] = []


def divide_into_pairs(team_list):
    # returns two lists of teams
    vacant_team_list = team_list[:]
    group_1 = []
    group_2 = []
    while len(vacant_team_list) > 0:
        group_1.append(vacant_team_list.pop(random.randrange(len(vacant_team_list))))
        group_2.append(vacant_team_list.pop(random.randrange(len(vacant_team_list))))
    return group_1, group_2


def lets_play(in_group_1, in_group_2):
    # simulating tour
    vacant_group_1 = {}
    vacant_group_2 = {}
    win_list = []
    for i in range(len(in_group_1)):
        vacant_group_1[in_group_1[i]] = random.randint(0, 6)
        vacant_group_2[in_group_2[i]] = random.randint(0, 6)

        teams[in_group_1[i]].append(in_group_2[i])
        teams[in_group_1[i]].append(vacant_group_1[in_group_1[i]])
        teams[in_group_1[i]].append(vacant_group_2[in_group_2[i]])

        teams[in_group_2[i]].append(in_group_1[i])
        teams[in_group_2[i]].append(vacant_group_2[in_group_2[i]])
        teams[in_group_2[i]].append(vacant_group_1[in_group_1[i]])

        if vacant_group_1[in_group_1[i]] == vacant_group_2[in_group_2[i]]:
            win_list.append(random.choice([in_group_1[i], in_group_2[i]]))
        elif vacant_group_1[in_group_1[i]] > vacant_group_2[in_group_2[i]]:
            win_list.append(in_group_1[i])
        else:
            win_list.append(in_group_2[i])
    # view of game
    for j in range(len(in_group_1)):
        print("{}:{} | {}:{} | Winner: {}".format(in_group_1[j], vacant_group_1[in_group_1[j]],
                                                  in_group_2[j], vacant_group_2[in_group_2[j]],
                                                  win_list[j]))
    return win_list


# Let's start!!
print("Start of championship!!!\n")
while len(l_teams) > 1:

    gr1, gr2 = divide_into_pairs(l_teams)

    if len(gr1) >= 2:
        print("1/{} tour results:".format(len(gr1)))
    else:
        print("Final result:")
    l_teams = lets_play(gr1, gr2)
    print()


if __name__ == '__main__':
    print('Enter \'exit\' for exit')
    print("Enter team name")

    while True:
        team_name = input()
        if team_name == 'exit':
            print('bye')
            exit()
        else:
            for key, value in teams.items():
                if key == team_name:
                    while len(value) > 0:
                        print("{} vs {} ({} : {})".format(key,
                                                          value.pop(0),
                                                          value.pop(0),
                                                          value.pop(0)))






