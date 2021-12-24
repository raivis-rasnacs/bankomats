import os
import time

#pin = "0000"
#bilance = 500

def datu_ielade():
  file = open("konta_dati.txt", "r")
  global pin, bilance
  pin = str(file.readline()).strip()
  bilance = int(file.readline())
  file.close()
  pin_parbaude()

def pin_parbaude():
  #os.system("clear")
  mans_pin = input("Ievadi pin kodu!")
  if mans_pin == pin:
    izvelne()
  else:
    print("Nepareizs pin kods!")
    pin_parbaude()

def izvelne():
  os.system("clear")
  print("*****BANKOMĀTS*****")
  print("1 - Iemaksāt naudu\n2 - Izmaksāt naudu\n3 - Apskatīt atlikumu\n4 - Mainīt pin kodu\n5 - Iziet")
  darbiba = int(input("Izvēlies darbību!"))
  if darbiba == 1:
    iemaksa()
  elif darbiba == 2:
    izmaksa()
  elif darbiba == 3:
    atlikums()
  elif darbiba == 4:
    pin_mainja()
  elif darbiba == 5:
    beigt_darbu()

def iemaksa():
  nauda = int(input("Ievadi summu, ko vēlies iemaksāt"))
  global bilance
  bilance = bilance + nauda
  print("Summa veiksmīgi iemaksāta!")
  time.sleep(1)
  izvelne()

def izmaksa():
  nauda = int(input("Ievadi summu, ko vēlies izņemt!"))
  global bilance
  if nauda <= bilance:
    bilance = bilance - nauda
    print("Saņem savu naudu!")
  else:
    print("Nepietiek naudas!")
  time.sleep(1)
  izvelne()

def atlikums():
  print("Tavs atlikums ir: ", bilance)
  time.sleep(1)
  izvelne()

def pin_mainja():
  vecaisPin = input("Ievadi esošo pin kodu")
  global pin
  if vecaisPin == pin:
    jaunaisPin = input("Ievadi jauno pin kodu!")
    if len(jaunaisPin) == 4:
      print("Pin kods nomainīts!")
      pin = jaunaisPin
    else:
      print("Operācijas kļūda. Jābūt 4 cipariem!")
  else:
    print("Kļūdains pin kods!")
  time.sleep(1)
  pin_parbaude()

def beigt_darbu():
  print("Visu labu! Gaidīsim atkal!")
  global pin, bilance
  file = open("konta_dati.txt", "w")
  file.write(str(pin)+"\n")
  file.write(str(bilance))
  file.close()
  #exit()
  
datu_ielade()