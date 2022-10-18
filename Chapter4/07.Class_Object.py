# Unit Class
class Unit:
    """
    Attr : name, health, shield, attack
    """

    # Constructor

    def __init__(self, name, health, shield, attack):
        self.name = name
        self.health = health
        self.shield = shield
        self.attack = attack
        print(f" [{self.name}](이)가 생성되었습니다. ")

    # str
    def __str__(self):
        return f"[{self.name}] HP : {self.health} Shield : {self.shield} Attack : {self.attack}"


# Probe Instance
probe = Unit("Probe", 20, 20, 5)

print(probe)
# Zeolot Instance
zeolot = Unit("Zeolot", 100, 60, 15)

print(zeolot)
# Dragon Instance
dragon = Unit("Dragon", 100, 80, 20)
print(dragon)
