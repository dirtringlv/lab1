class Weapon:
   def __init__(self,damage,weight,range,description):
       self.damage=damage
       self.weight=weight
       self.range=range
       self.description=description

   def attack(self):
       print('do smth')

class LongRange(Weapon):
    def __init__(self,accuracy):
        self.accuracy=accuracy

 class  CloseRange(Weapon):
     def __init__(self,speed,isAmmoRequired,attackMethod):
         self.speed=speed
         self.isAmmoRequired=isAmmoRequired#для оружия с "боезапасом". Бензопила, например
         self.attackMethod=attackMethod#колющее, режущее и тд
 class Knife(CloseRange)
     def __init__(self,sharpness,bladeLength):
         self.sharpness=sharpness
         self.bladeLength=bladeLength

 class Chainsaw(CloseRange):
     def __init__(self,ammo):
         self.ammo=ammo


 class Throwing(LongRange)
     def __init__(self,throwingDistance):
         self.throwingDistance=throwingDistance

 class ThrowingKnife(Throwing,Knife):
     def __init__(self):


 class Grenade(Throwing):
     def __init__(self,actionRange):
         self.actionRange=actionRange


 class FragGrenade(Grenade):
     def __init__(self):


 class Firearms(LongRange):
     def __init__(self):

 class Pistol