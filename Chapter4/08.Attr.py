class Unit:
    """
    Attr : name, health, shield, attack
    """

    # class Attribute
    count = 0

    def __init__(self, name, health, shield, attack):

        # object Attribute
        self.name = name
        self.__health = health # private Attribute
        self.shield = shield
        self.attack = attack
        Unit.count += 1
        print(f" [{self.name}](이)가 생성되었습니다. ")

    def __str__(self):
        return f"[{self.name}] HP : {self.__health} Shield : {self.shield} Attack : {self.attack}"


probe = Unit("Probe", 20, 20, 5)

zeolot = Unit("Zeolot", 100, 60, 15)

dragon = Unit("Dragon", 100, 80, 20)

# 인스턴스 속성 수정
probe.attack += 1
print(probe)

# 전체 유닛개수
print(Unit.count)

# 비공개 속성
probe.__health = 9999
print(probe)

# 접근(Name 맹글링)
probe._Unit__health = 9999
print(probe)