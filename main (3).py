class Player(object):
    def __init__(self, name, age, skills, style=None):
        self.name = name
        self.age = age
        self.skills = skills
        self.style = style

    def get_player(self):
        print(self.name,self.age,self.skills,self.style)


class Team(object):
    def __init__(self, name):
        self.name = name
        self._players = []

    def add_player(self, obj):
        if isinstance(obj, Player):
            self._players.append(obj)
        else:
            print("Please provide player object")

    def get_players(self):
        for player in self._players:
            player.get_player()


if __name__ == "__main__":

    p1 = Player("Arul", 34, "Wicket Kipper", "Left-Hand Batsman")
    p2 = Player("pugazh", 35, "Batsman", "Right-Hand Batsman")
    p3 = Player("Arjun", 32, "Bauwller", "Left-Hand Bauwller")
    p4 = Player("Raja", 31, "Bauwller", "Medium Pace Bauwller")
    p5 = Player("Maya", 33, "All rounder")

    t = Team("India")
    t.add_player(p1)
    t.add_player(p2)
    t.add_player(p3)
    t.add_player(p4)
    t.add_player(p5)

    t.get_players()