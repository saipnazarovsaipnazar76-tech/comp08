# class Person():
#     ism = 'Saipnazar'
#     familiya = 'Saipnazarov'
#     yosh = '15'
#     manzil = "Xiva Shahar"
#     kasb = 'Oquvchi'
# print(Person.ism)

class Person():
    def _init_(self,ism,familiya,yosh,ish_joyi,manzil,):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.ish_joyi = ish_joyi
        self.manzil = manzil 
    def __init__(self):
        return f'ismi --> {self.ism}\nfamiliya--> {self.familiya}\nyoshi--> {self.yosh}\nish_joyi--> {self.ish_joyi}\nmanzil--> {self.manzil}'

p1 = Person('Mustafo','Polvanazirov',17,'ishsiz','Xiva Shahar')
p2 = Person('Saipnazar','Saipnazarov',15,'ishsiz','Xiva Shahar')
p3 = Person('Azizbek','Atobayev',13,'ishsiz','Xiva Shahar')
print(p1)
print(p2)
print(p3)

# class Talaba():
#     def __init__(self,ism,familiya,yosh,universitet,kurs,):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.universitet = universitet
#         self.kurs = kurs
#     def __str__(self):
#         return f' ism--> {self.ism}\nfamiliya--> {self.familiya}\nyosh--> {self.yosh}\nuniversistet--> {self.universitet}\nkurs--> {self.kurs}'

# p1 = Talaba('Ali','Valiyev','20','TATU','3')
# print(p1)


































































































