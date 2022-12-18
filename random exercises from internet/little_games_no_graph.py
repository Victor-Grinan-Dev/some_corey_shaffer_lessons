import random


class NoGraphGames:

    @staticmethod
    def Rock_Paper_Scissors(self):
        RPS_dict = {1: "rock", 2: "paper", 3: "scissors"}
        Ia_point = 0
        userpoint = 0
        while True:
            answer = int(input(f"\n{RPS_dict}\ninput \"0 (Zero)\" to exit.\n0-3 choice input: "))
            IA_answer = random.randint(1, 3)
            if answer == IA_answer:
                print(f"\nyour answer: {RPS_dict[answer]} , computer answer: {RPS_dict[IA_answer]}")
                print("******* TIE! *******")
            elif answer == 0:
                break
            elif answer in RPS_dict:
                print(f"\nyour answer: {RPS_dict[answer]} , computer answer: {RPS_dict[IA_answer]}")
                winner, userpoint, Ia_point = NoGraphGames.Comparar_manos(answer, IA_answer, userpoint, Ia_point)
                print(f"{winner}")
            else:
                print("invalid answer")
            print(f"user: {userpoint} computer: {Ia_point}")

    @staticmethod
    def Comparar_manos(user, IA, userpoint, Ia_point):
        result = str(user) + str(IA)
        result = int(result)
        logic = {12: "you loose!!\n******LOOSER******", 13: "******you win******", 21: "******you win******",
                 23: "you loose!!\n******LOOSER******", 31: "you loose!!\n******LOOSER******",
                 32: "******you win******"}
        if result in logic:
            winner = logic[result]
            if "you loose" in winner:
                Ia_point += 1
            elif "you win" in winner:
                userpoint += 1

            return winner, userpoint, Ia_point

    @staticmethod
    def guess_my_number(self):
        score = {"user": 0, "computer": 0}
        answer = ""
        handicap = 3
        while answer != "exit":
            num = str(random.randint(1, handicap))
            answer = input(f"\ntype exit to stop program\nfrom 1-{handicap} guess my number:")
            if answer == "exit":
                print(f"\n******FINAL SCORE {score}******")
                break
            elif answer == num:
                print("CONGRATS!! you win")
                score["user"] += 1
            elif answer in range(1, handicap):
                print("you loose", end=" ")
                if int(answer) < int(num):
                    print(f"...too LOW, number was {num}")
                if int(answer) > int(num):
                    print(f"...too HIGH, number was {num}")
                score["computer"] += 1
            else:
                print("invalid input")
