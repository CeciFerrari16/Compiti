# Aggiungere i livelli:
# dopo un numero di score o gold si passa al livello successivo. Completati si ha la schermata di vittoria.
import os
from random import choice

DIRECTIONS = "up", "down", "left", "right"

class Entity: 
  def __init__(self, x, y, field, graphic):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)
    self.graphic = graphic

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

    if self.x == futureX and self.y == futureY:
      return

    e = self.field.get_entity_at_coords(futureX, futureY)

    if e == None:
      self.x = futureX
      self.y = futureY
    else:
      self.collide(e)

  def collide(self, entity):
    pass

  def update(self):
    pass

class Gold(Entity):
  def __init__(self, x, y, field):
    super().__init__(x, y, field, "$")
    self.value = 100

class Wall(Entity):
  def __init__(self, x, y, field):
    super().__init__(x, y, field, "#")

class Living_Entity(Entity):
  def __init__(self, x, y, name, hp, damage, field, graphic):
    super().__init__(x, y, field, graphic)
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.damage = damage

  def info(self):
    print("sono", self.name, "hp:", self.hp, "/", self.max_hp, "e mi trovo a", self.x, ",", self.y)

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

class Monster(Living_Entity):
  def __init__(self, x, y, name, field):
    super().__init__(x, y, name, 10, 5, field, "m")
    
  def collide(self, entity):
    if isinstance(entity, Player):
      self.attack(entity)
  
  def move(self):
    super().move(choice(DIRECTIONS))

  def update(self):
    super().update()
    self.move()

class Player(Living_Entity):
  def __init__(self, x, y, name, field):
    super().__init__(x, y, name, 20, 5, field, "p")
  
  def collide(self, entity):
    if isinstance(entity, Monster):
      self.attack(entity)
    elif isinstance(entity, Gold):
      self.field.score += entity.value
      self.field.entities.remove(entity)

class Field:
  def __init__(self, levelNumber):
    self.entities = []
    self.score = 0
    self.levelNumber = levelNumber
    self.levelTot = 3
    self.goldNumber = 0

    f = open("./level" + str(levelNumber) + ".level", "r")
    rows = f.read().split("\n")
    f.close()

    self.h = len(rows)
    self.w = len(rows[0])

    for y in range(self.h):
      row = rows[y]
      for x in range(self.w):
        char = row[x]
        if char == "p":
          self.player = Player(x, y, "Player", self)
        elif char == "#":
          Wall(x, y, self)
        elif char == "$":
          Gold(x, y, self)
          self.goldNumber += 1
        elif char == "m":
          Monster(x, y, "Monster", self)

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

    return None
  
  def check_score(self, value):
    if self.score == self.goldNumber * value:
      print("Great job, you can level up!")
      print("Digit:", self.levelNumber + 1)
      return True
    else:
      pass
    
  def check_victory(self, number):
    if number == self.levelTot:
      clear_screen()
      print("YOU WON THE GAME!!")
      print("thank you for playing <3")
      return True
    else: pass

  def draw(self):
    print("level:", self.levelNumber)
    print("n° golds:", self.goldNumber)
    print("score:", self.score)
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[" + e.graphic + "]", end = "")
            break    
        else:
          print("[ ]", end = "")
      print()
    if self.levelNumber == self.levelTot:
      print("This is the last level!")
    else: pass
  
  def update(self):
    for e in self.entities:
      e.update()

field = Field(1)

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

completed = 0
clear_screen()
while True: 
  field.update()
  field.draw()
  pass1 = field.check_score(100) # level completed
  if pass1 == True:
    completed = field.levelNumber

  if field.check_victory(completed) == True: # victory
    break
  command = input("input: ").lower()
  clear_screen()
  
  if command == "q": break
  elif command == "w": field.player.move("up")
  elif command == "a": field.player.move("left")
  elif command == "s": field.player.move("down")
  elif command == "d": field.player.move("right")
  elif command.isnumeric() == True : 
    if pass1 == True:
      field.levelNumber = int(command)
      field = Field(field.levelNumber)
    else: print("Devi finire prima questo livello!")