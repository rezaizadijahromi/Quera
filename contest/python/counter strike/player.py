class Player:
    def __init__(self, name, team, enter_time):
        # self.guns = Gun()
        self.name = name
        self.team = team
        self.enter_time = enter_time
        self.guns = [{
            "knife": "knife", "type": "knifes", "time": "00:00:00"
        }]
        self.money = 1000
        self.health = 100
        self.living = True
        self.killed = 0
        self.kills = 0
        self.game_guns = {
            "terrorist": {
                "heavy_gun": {
                    "AK": {
                        "price": 2700,
                        "deadly": 31,
                        "earning": 100
                    },
                    "AWP": {
                        "price": 4300,
                        "deadly": 110,
                        "earning": 50
                    }
                },
                "pistol": {
                    "Revolver": {
                        "price": 600,
                        "deadly": 51,
                        "earning": 150
                    },
                    "Glock-18": {
                        "price": 300,
                        "deadly": 11,
                        "earning": 200
                    }
                }
            },
            "Counter-terrorist": {
                "heavy_gun": {
                    "M4A1": {
                        "price": 2700,
                        "deadly": 29,
                        "earning": 100
                    },
                    "AWP": {
                        "price": 4300,
                        "deadly": 110,
                        "earning": 50
                    }
                },
                "pistol": {
                    "Desert-Eagle": {
                        "price": 600,
                        "deadly": 53,
                        "earning": 175
                    },
                    "UPS-S": {
                        "price": 300,
                        "deadly": 13,
                        "earning": 225
                    }
                }
            }
        }

    def get_name(self):
        return self.name

    def get_living(self):
        return self.living
