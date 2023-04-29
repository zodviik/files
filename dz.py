class BaseCharacter():
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
    def move(self, delta_x, delta_y):
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.pos_x = delta_x
        self.pos_y = delta_y
    def is_alive(self):
        if self.hp <= 0:
            return True
        else:
            return False
    def get_damage(self, amount):
        self.amount = amount
        self.hp -= amount
    def get_coords(self):
        coords = [self.pos_x, self.pos_y]
        print(coords)
class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
       self.pos_x = pos_x
       self.pos_y = pos_y
       self.name = name
       self.hp = hp
    def hit(self, target):
        self.target = target
        if type(self.target) != BaseEnemy:
            print("Я могу ударить только врага")
                      
class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.weapon = weapon
        self.hp = hp
    def hit(self, target):
        self.target = target
        if type(self.target) != MainHero:
            print("Я могу ударить только Главного героя")
    def pr(self):
        coord_enemy = f"Враг на позиции {self.pos_x, self.pos_y} с оружием {BaseEnemy.weapon}"

class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
    def hit(self, actor, target: BaseEnemy):
        if target.hp <= 0:
            print("Враг уже повержен")
        elif MainHero.pos_x - BaseEnemy.pos_x > Weapon.range or MainHero.pos_y - BaseEnemy.pos_y > Weapon.range:
            print(f"Враг слишком далеко для оружия {Weapon.name}")
        else:
            print(f"Врагу нанесён оружием {Weapon.name} в размере {Weapon.damage}")
            target.hp -= Weapon.damage 
    def k():
        return Weapon.name
weapon1=Weapon("короткий меч",5,1)
weapon2=Weapon("длинный меч",7,2)
weapon3=Weapon("лук",3,10)
weapon4=Weapon("лазерная орбитальная пушка",1000,1000)
princess=BaseCharacter(100,100,100)
arcger=BaseEnemy(50,50,weapon3,100)
armored_swordsman=BaseEnemy(50,50,weapon2,500)
arcger.hit(armored_swordsman)
armored_swordsman.move(10,10)
print(armored_swordsman.get_coords())
main_hero=MainHero(0,0,"Король Артур",200)
main_hero.hit(armored_swordsman)
