class Unit:
    """
    Attr : name, health, shield, attack
    """

    count = 0

    # Magic method
    def __init__(self, name, health, shield, attack):

        self.name = name
        self.__health = health
        self.shield = shield
        self.attack = attack
        Unit.count += 1
        print(f" [{self.name}](이)가 생성되었습니다. ")

    def __str__(self):
        return f"[{self.name}] HP : {self.__health} Shield : {self.shield} Attack : {self.attack}"

    # Instance Method
    # 인스턴스 속성에 접근할 수 있는 메소드
    def hit(self, attack):
        if attack <= self.shield:
            self.shield = self.shield - attack
            print(f"[{self.name}이 공격을 받습니다.] HP: {self.__health} Shield: {self.shield}")
        elif self.__health > attack > self.shield:
            self.__health = self.__health + (self.shield - attack)
            self.shield = 0
            print(f"[{self.name}이 공격을 받습니다.] HP: {self.__health} Shield: 0")
        elif attack > self.__health:
            self.__health = 0
            print(f"[{self.name}이 죽었습니다..] HP: 0 Shield: 0")

    # class Method
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛개수 : [{cls.count}]개")


probe = Unit("Probe", 20, 20, 5)

zeolot = Unit("Zeolot", 100, 60, 15)

dragon = Unit("Dragon", 100, 80, 20)
print("================================")
probe.hit(dragon.attack)
probe.hit(zeolot.attack)
probe.hit(dragon.attack)
print(probe)

print("================================")
Unit.print_count()