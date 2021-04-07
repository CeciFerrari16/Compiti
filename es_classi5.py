import os
from random import randint

all_dir = ["up", "down", "left", "right"]

def random_element(lista):
  number = randint(0, len(lista) - 1)
  random_element = lista[number]
  return str(random_element)

class Entity: 
  def __init__(self, x, y, field, skin = "[x]"):
    self.x = x
    self.y = y
    self.skin = skin
    self.field = field
    self.field.entities.append(self)

  def move(self, direction):
    futureX = self.x
    futureY = self.y

    if direction == "up" and self.y > 0:
      futureY -= 1
    elif direction == "down" and self.y < self.field.h - 1:
      futureY += 1
    elif direction == "left" and self.x > 0:
      futureX -= 1
    elif direction == "right" and self.x < self.field.w - 1:
      futureX += 1

    e = self.field.get_entity_at_coords(futureX, futureY)

    if e == None:
      self.x = futureX
      self.y = futureY
    else:
      self.collide(e)

  def collide(self, entity):
    pass

class Monster(Entity):
  def __init__(self, x, y, name, damage, field, skin = "[x]"):
    super().__init__(x, y, field, skin)
    self.name = name
    self.hp = 10
    self.damage = damage

  def info(self):
    print("sono", self.name, "hp:", self.hp, "/10", "e mi trovo a", self.x, ",", self.y)

  def attack(self, enemy):
    if self.hp <= 0:
      print(self.name, "prova ad attaccare da morto con scarsi risultati")
    else: 
      print(self.name, "attacca", enemy.name)

      if (enemy.hp <= 0):
        print(enemy.name, "e' morto")
        self.field.entities.remove(enemy)
      else:
        enemy.hp -= self.damage
  
  def collide(self, entity):
    self.attack(entity)

class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
    self.entities = []

  def get_entity_at_coords(self, x, y): #trovare il nome dell'entità vicina
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

    return None
    
  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print(e.skin, end = "")
            break    
        else:
          print("[ ]", end = "")
      print()

field = Field()
m1 = Monster(2, 2, "Paolo", 10, field)
m2 = Monster(1, 1, "Giorgio", 10, field)
p = Monster(0, 0, "Player", 4, field, "[o]")

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

clear_screen()
while True:  #comandi player
  field.draw()

  command = input("input: ").lower()

  #num_e = len(field.entities)
  m1.move(random_element(all_dir))
  m2.move(random_element(all_dir))
  #if num_e == 1:
  #  break 
  clear_screen()

  if command == "q":
    break
  elif command == "w":
    p.move("up")
  elif command == "a":
    p.move("left")
  elif command == "s":
    p.move("down")
  elif command == "d":
    p.move("right")

