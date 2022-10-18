from abc import *


class Item(metaclass=ABCMeta):
    """
    Attr: name,
    Method: drow, drop
    """

    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def drop(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    @abstractmethod
    def use(self):
        pass


class Weapon(Item):
    """
    Attr: demage
    metho: attack
    """
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage

    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.")


class HealingItem(Item):
    """
    Attr: recovery_aomount
    method: use
    """
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 사용합니다. {self.recovery_amount} 회복")


m16 = Weapon("m16", 110)
band = HealingItem("붕대", 20)

m16.use()
band.use()

