#  Each game last for 02:15:00
# if no one survive counter-terrorist wine
# if no one enter the game counter-terrorist wine
# Each player can have a heavy gun and one belt gun
# in default all the players have a knife
# buying last just for 45 sec after game starts 00:45:00
# Start health 100 health == 0 means dead

from player import Player


class Game:
    def __init__(self):
        self.player = Player()
        self.terrorist_team = []
        self.counter_terrorist_team = []

    def add_to_team(self):
        # TODO if added time was after 00:00:00 living must be false
        if self.player in self.terrorist_team or self.player in self.counter_terrorist_team:
            print("you are already in this game")
        else:
            if self.player.team == "Terrorist":
                if len(self.terrorist_team) == 10:
                    print("this team is full")
                    self.counter_terrorist_team.append(self.player)
                else:
                    self.terrorist_team.append(self.player)
            elif self.player.team == "Counter-Terrorist":
                if len(self.counter_terrorist_team) == 10:
                    self.counter_terrorist_team.append(self.player)
                else:
                    self.counter_terrorist_team.append(self.player)

    def get_money(self):
        # TODO add time to function argument
        for (counter_terrorist, terrorist) in zip(self.counter_terrorist_team, self.terrorist_team):
            if self.player.get_name() != counter_terrorist or self.player.get_name() != terrorist:
                print("invalid username")
        print(self.player.money)

    def get_health(self):
        # TODO add time to function argument
        for (counter_terrorist, terrorist) in zip(self.counter_terrorist_team, self.terrorist_team):
            if self.player.get_name() != counter_terrorist or self.player.get_name() != terrorist:
                print("invalid username")

        if self.player.get_living():
            print(f"{self.player.health}")
        else:
            print(0)

    def buy_gun(self, time, gun_name, gun_type):
        # TODO Implementing time conditions
        success = False
        if self.player in self.terrorist_team or self.player in self.counter_terrorist_team:
            if self.player.living:
                if self.player.team == "Counter-terrorist":
                    counter_terroris = self.player.game_guns["Counter-terrorist"]
                    for i in counter_terroris:
                        if i == gun_type:
                            if i not in self.player.guns[i]:
                                for j in counter_terroris[i]:
                                    if self.player.money >= counter_terroris[i][j]["price"]:
                                        if j == gun_name:
                                            temp = dict()
                                            gun = dict()
                                            temp[gun_name] = counter_terroris[i][j]
                                            gun[gun_type] = temp
                                            success = True
                                            self.player.guns.append(gun)
                                        else:
                                            print("invalid category gun")
                                    else:
                                        print("no enough money")
                            else:
                                print(f"you have a {i}")
                elif self.player.team == "Terrorist":
                    terrorist = self.player.game_guns["terrorist"]
                    for i in terrorist:
                        if i == gun_type:
                            if i not in self.player.guns[i]:
                                for j in terrorist[i]:
                                    if self.player.money >= terrorist[i][j]["price"]:
                                        if j == gun_name:
                                            temp = dict()
                                            gun = dict()
                                            temp[gun_name] = terrorist[i][j]
                                            gun[gun_type] = temp
                                            success = True
                                            self.player.guns.append(gun)
                                        else:
                                            print("invalid category gun")
                                    else:
                                        print("no enough money")
                            else:
                                print(f"you have a {i}")
            else:
                print("deads can not buy")
        else:
            print("invalid username")

        if success:
            print("I hope you can use it")
            return

    def tap(self, attacker, attacked, gun_type, time):
        # TODO Implementing time
        if attacked in self.counter_terrorist_team and attacked in self.counter_terrorist_team or attacker in self.counter_terrorist_team and attacked in self.counter_terrorist_team:
            # TODO return team and existense
            attacker_info = self.get_payer_info(attacker)
            attacked_info = self.get_payer_info(attacked)
            if not attacked_info.get_living():
                print("attacked is dead")
                return
            elif not attacker_info.get_living():
                print("attacker is dead")
                return
            elif attacker_info.team == attacked_info.team:
                print("friendly fire")
                return
            elif gun_type not in attacker_info.guns:
                print("no such gun")
                return
        else:
            print("invalid username")
            return

        return "nice shot"

    # helper function
    def get_payer_info(self, name):
        for counter_terrorist, terrorist in zip(self.counter_terrorist_team, self.terrorist_team):
            if counter_terrorist.name == name:
                return counter_terroris
            elif terrorist.name == name:
                return terrorist
            else:
                return "not found"


obj = Player("reza", "Counter-terrorist", "00:00:00")
counter_terroris = obj.game_guns["Counter-terrorist"]
# print(len(counter))
# for i in range(len(counter)):
#     print(counter["heavy_gun
# g = []
# for i in counter_terroris:
#     if i == "heavy_gun":
#         # print(counter_terroris[i])
#         for j in counter_terroris[i]:
#             if j == "AWP":
#                 d = dict()
#                 h = dict()
#                 d["AWP"] = counter_terroris[i][j]

#                 h["heavy_gun"] = d
#                 g.append(h)
# print(counter_terroris[i][j])
# print(g[0])
