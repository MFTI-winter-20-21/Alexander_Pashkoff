import random
player_count_1 = 0
player_count_2 = 0
player_count_3 = 0
win1 = False
win2 = False
win3 = False
name1 = input("Player first name   ")
name2 = input("Player first name   ")
name3 = input("Player first name   ")
deaf1 = False
deaf2 = False
deaf3 = False
want1 = False
want2 = False
want3 = False
above1 = False
above2 = False
above3 = False
print("Если хотите взять карту пишите да, если не хотите пишите нет")
while deaf1 or above1 or win1 != True or deaf2 or above2 or win2 != True or deaf3 or above3 or win3 != True:
    if  above1 == False and deaf1 == False:
        print("ХОД ", name1)
        want1 = input("Берёте карту? ")
        if want1 == "да":
            player_count_1 = player_count_1 + random.randint(1,10)
            print("Ваше количество очков", player_count_1)
            if player_count_1 > 21:
                print("Ваши очки превышают 21",name1,"проиграл")
                deaf1 = True
            elif player_count_1 == 21:
                print("Читер или нет, но ты  выиграл", name1, "победил")
                win1 = True

        else:
            print(name1,"вышел из игры со счётом",player_count_1)
            above1 = True
    if  above2 == False and deaf2 == False:
        print("ХОД ", name2)
        want2 = input("Берёте карту? ")
        if want2 == "да":
            player_count_2 = player_count_2 + random.randint(1,10)
            print("Ваше количество очков", player_count_2)
            if player_count_2 > 21:
                print("Ваши очки превышают 21",name2,"проиграл")
                deaf2 = True
            elif player_count_2 == 21:
                print("Читер или нет, но ты  выиграл", name2, "победил")
                win2 = True

        else:
            print(name2,"вышел из игры со счётом",player_count_2)
            above2 = True
    if  above3 == False and deaf3 == False:
        print("ХОД ", name3)
        want3 = input("Берёте карту? ")
        if want3 == "да":
            player_count_3 = player_count_3 + random.randint(1,10)
            print("Ваше количество очков", player_count_3)
            if player_count_3 > 21:
                print("Ваши очки превышают 21",name3,"проиграл")
                deaf2 = True
            elif player_count_3 == 21:
                print("Читер или нет, но ты  выиграл", name3, "победил")
                win3 = True

        else:
            print(name3,"вышел из игры со счётом",player_count_3)
            above3 = True
if player_count_1 :

print("Конец")



