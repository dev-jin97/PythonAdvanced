
"""
Player class를 구현
Attr: nickname, mineral, gas, unitList
"""

unit_info = {
    "probe": {
        "name": "프로브",
        "mineral": 50,
        "gas": 0,
        "hp": 20,
        "shield": 20,
        "demage": 5
    },
    "zeolot": {
        "name": "질럿",
        "mineral": 100,
        "gas": 0,
        "hp": 100,
        "shield": 60,
        "demage": 16
    },
    "dragon": {
        "name": "드라군",
        "mineral": 125,
        "gas": 50,
        "hp": 100,
        "shield": 80,
        "demage": 20
    }
}

"""
produce(이름, 미네랄, 가스, 체력, 방어막, 공격력)
"""


class Player:
    """
    Attr: name, mineral, gas, unitlist
    """
    def __init__(self, name, mineral, gas):
        self.name = name
        self.mineral = mineral
        self.gas = gas
        self.unit_list = list()

    def print_info(self):
        print(f"[{self.name}] M : {self.mineral} G: {self.gas} UNIT : {self.unit_list}")

    def produce(self, unit_name):
        """
        Produce_unit
        """
        unit_obj = unit_info[unit_name]

        mineral = self.mineral - unit_obj["mineral"]
        gas = self.gas - unit_obj["gas"]
        if mineral >= 0 and gas >= 0:
            self.unit_list.append(unit_obj["name"])
            self.mineral = mineral
            self.gas = gas
            print(f"유닛이 생성되었습니다. - {unit_obj['name']}")
        elif mineral < 0 and gas < 0:
            print("두 자원(미네랄, 가스) 모두 부족합니다.")
        elif mineral < 0:
            print("미네랄이 부족합니다.")
        elif gas < 0:
            print("가스가 부족합니다.")


hyeonJin = Player("hyeonjin", 400, 50)
hyeonJin.print_info()
hyeonJin.produce("dragon")
hyeonJin.print_info()
hyeonJin.produce("zeolot")
hyeonJin.print_info()
hyeonJin.produce("dragon")




