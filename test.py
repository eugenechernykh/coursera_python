import random

random.seed(3)


class Assign:
    def __init__(self, value=0):
        self.__value = value


obj1 = Assign(2)
obj2 = Assign(2)

print(obj1, obj2)
print(id(obj1) == id(obj2), end=' ')

str1 = 'Good'
str2 = 'Good'

print(id(str1) == id(str2))

str = 'good-BYE'
print(str.capitalize())

fist_hero = random.choice(pictures)
second_hero = random.choice(pictures)
while fist_hero == second_hero:
    second_hero = random.choice(pictures)
heroes1 = (fist_hero, second_hero)

for pic in pictures:
    hero = pygame.transform.scale(hero, (15, 20))
