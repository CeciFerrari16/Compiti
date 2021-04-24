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
    self.status = "alive"

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
        self.field.enemyRemain -= 1
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
      self.field.goldRemain -= 1

class Field:
  def __init__(self, levelNumber):
    self.entities = []
    self.score = 0
    self.levelNumber = levelNumber
    self.levelTot = 4
    self.goldNumber = 0
    self.enemyNumber = 0

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
          self.gold = Gold(x, y, self)
          self.goldNumber += 1
        elif char == "m":
          self.enemy = Monster(x, y, "Monster", self)
          self.enemyNumber += 1
    
    self.goldRemain = self.goldNumber
    self.enemyRemain = self.enemyNumber

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

    return None
  
  def check_score(self):
    if self.score == self.goldNumber * self.gold.value:
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
  
  def check_enemy(self):
    if self.enemyRemain == 0:
      return True
    else: pass
  
  def check_death(self):
    if self.player.hp <= 0:
      self.player.status = "dead"
      return True
    else: pass
  
  def info_level(self):
    print("level:", self.levelNumber)
    print("n° golds:", self.goldRemain, "/", self.goldNumber)
    print("n° enemies:", self.enemyRemain, "/", self.enemyNumber)
    print("status:", self.player.status)

  def draw(self):
    print("score:", self.score)
    print("hp:", self.player.hp)
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

def restart(decision = "yes"):
  if decision == "yes":
      exec(open("./es_classi7.py").read())
  else:
      print("Ok, thank you for playing!")
  
reward = 0
completed = 0
clear_screen()
while True: 
  field.update()
  field.draw()

  pass1 = field.check_score() # level completed
  if pass1 == True:
    completed = field.levelNumber
  
  if field.check_death() == True:
    clear_screen()
    print("GAME OVER")
    print("If you want to restart tap 'r'")
  
  if field.check_enemy() == True and reward == 0:
    field.player.hp += 10
    reward += 1

  if field.check_victory(completed) == True: # victory
    break

  command = input("input: ").lower()
  clear_screen()
  
  if command == "q": break
  elif command == "r": restart()
  elif field.check_death() != True:
    if command == "w": field.player.move("up")
    elif command == "a": field.player.move("left")
    elif command == "s": field.player.move("down")
    elif command == "d": field.player.move("right")
    elif command == "r": restart()
    elif command == "i": 
      field.info_level()
      reply = input("Write 'y' if you are ready to continue: ").lower()
      if reply == "y": continue
    elif command.isnumeric() == True and int(command) == field.levelNumber + 1: 
      if pass1 == True and field.check_death() != True:
        reward = 0
        field.levelNumber = int(command)
        hp = field.player.hp 
        field = Field(field.levelNumber)
        field.player.hp = hp  
      else: print("You MUST finish this level before change it!")
    else: pass