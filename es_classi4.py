# Lezione sulle classi
import os
from random import randint

all_dir = ["up", "down", "left", "right"]

def list_trick(list1, e):
  list1.remove(e)
  list2 = list1
  list1.append(e)
  return list2

def random_element(lista):
  number = randint(0,len(lista) - 1)
  random_element = lista[number]
  return random_element

class Entity:
  def __init__(self, x, y, field): #inizializzando l'istanza con il costruttore init
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self) #aggiungo entity alla lista entities del field
  
  def move(self, direction):
    controllo = self.check_collision()
    if direction == "up" and self.y > 0 and controllo != "not up":
      self.y -= 1
    elif direction == "down" and self.y < self.field.h - 1 and controllo != "not down":
      self.y += 1
    elif direction == "left" and self.x > 0 and controllo != "not left":
      self.x -= 1
    elif direction == "right" and self.x < self.field.w - 1 and controllo != "not right":
      self.x += 1
    elif controllo == "not up" or controllo == "not down" or controllo == "not left" or controllo == "not right":
      print(self.name_collision, "ti sbarra la strada")
    else:
      print("L'entità non può muoversi nella direzione richiesta")

  def check_collision(self, name_collision = "Un'entità"):
    lista = list_trick(field.entities, self)
    for e in lista:
      #print(e.x, e.y)
      if self.x == e.x and self.y == e.y + 1: #up
        self.name_collision = e.name #sbarra la strada per l'alto
        return "not up"
      elif self.x == e.x and self.y == e.y - 1: #down
        self.name_collision = e.name #sbarra la strada per giù
        return "not down"
      elif self.x == e.x - 1 and self.y == e.y: #left
        self.name_collision = e.name #sbarra la strada da sinistra
        return "not left"
      elif self.x == e.x + 1 and self.y == e.y: #right
        self.name_collision = e.name #sbarra la strada da destra
        return "not right"
      else:
        return True
        

class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name 
    self.hp = 20 # vita
    self.damage = damage

  def info(self):
    print("sono", self.name, "hp:", self.hp, "/20", "e mi trovo a (", self.x, ",", self.y, ")")

  def attack(self, enemy):
    if self.hp <= 0:
      print("non è possibile attaccare,", self.name, "è morto")
    else:
      print(self.name, "attacca", enemy.name)

      if enemy.hp <= 0:
        print(enemy.name, "è morto")
      else:
        enemy.hp -= self.damage

class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
    self.entities = []

  def draw(self):
    #os.system("clear")
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[+]", end = "")
            break
        else: # nel ciclo for di e
          print("[ ]", end = "")
      print()
    print()
      

field = Field() # creo il campo
m = Monster(2, 2, "Paolo", 10, field)
m1 = Monster(1, 1, "Giorgio", 10, field)
field.draw()

m1.move("right")
field.draw()
#print(m1.x, m1.y)
m1.move("down")
field.draw()
#print(m1.x, m1.y)
m1.move("down")
field.draw()
#print(m1.x, m1.y)
