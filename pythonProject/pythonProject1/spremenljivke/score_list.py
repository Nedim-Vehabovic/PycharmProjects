import random
import json
import datetime
current_time = datetime.datetime.now()
secret = random.randint(1, 10)
attempts = 0
name = input("Vnesite svoje ime: ")


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("top_score: " + str(score_list))

for score_dict in score_list:
    player = "Player {0} had {1} attempts. The secret number was {2}. Imel je {3} napačnih ugibanj".format(score_dict.get("name"),
                                                                            score_dict.get("attempts"),
                                                                            score_dict.get("secret number"),
                                                                             score_dict.get("wrong guess"))
    print(player)

uns_guess = []
while True:
    attempts = attempts + 1
    guess = int(input("Uganite pravilno številko: "))

    if guess == secret:
        score_list.append({"name" : name,"attempts": attempts, "datum": str(datetime.datetime.now()),"secret number": secret, "wrong guess": uns_guess})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list,indent=1))
        print("***********Čestitamo********. Uganili ste previlno številko.")
        print("Bila je številka {1}. To je bil vaš {0} poizkus" .format(attempts, guess))
        break
    elif guess < secret:
        print("Napačna številka. Poizkusite z večjim številom.")
        print("To je bil vaš {0} poizkus" .format(attempts))

    else:
        print("Napačna številka. Poizkusite z manjšim številom.")
        print("To je bil vaš {0} poizkus" .format(attempts))

    uns_guess.append(guess)
