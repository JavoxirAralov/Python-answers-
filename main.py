print("Hello world!")
"""
bu izoh kop qatorli izox uchun ishlatildi

"""
# va agar biz  mayda bir qatorli izox ishlatsak shunaa yozamiz;
"""
a=2
b=3
c=a+b
print(c)
y="salom"
x=5
print(x,y)
"""

"""
# turli ozgarivchilarda oson ishlash yolari : 
x,y,a = "OLMA","BANAN", 3
print (x)
print (y)
print (a)
"""
"""
 # --- bita qiymatni bir necha ozgarvchiga yuklash
 x = y =  a = "olma"
 print(x)
 print(y)
 print(a)
 """

"""
# --- python dasturlash tilida print () bu buror sozni ekranga chiqarish uchun foydalaniladi; c++ da cout " "; dek
print ( "assalomu alekum")
# + belgisi bilan printni ichiga narsa qoshishimiz mumkin boladi
x = " alekum "
print ( " assalomu"+x)

"""

""" 
# bunday hollarda  ishlash xato chunki x=5 bu int tipidagi son bolibv uni
# string tipiga otkazib bolmaydi agar biz x=5 ni string tipiga otkazmoqchi bolsak '5 ' shunaqa yozami
 
 # x=5
 # x='5'
y= " java "
print (x+y)


# global ozgarivchi ochish va funkitsiya ichida va tashqatrisida ishlatish

x =" qiziq"
def funksiya():
    print("dasturlash"+x)
    funksiya()
    """

"""
# arifmetik amallar bilan ishlash

x = 10
y = 3
print (x+y)
print (x-y)
print (x*y)
print (x/y)
print (x%y)
print (x//y)
print (x**y)
"""
"""
# mantiqiy operatorlar bilan ishlash
# == teng
# != teng emas
#  < katta
# > kichik
# <= katta yoki teng
# >= kichik yoki teng

# taqoslash operatorlari c++
 # va =&   python and
 # yoki  ||    python or
 # yoq  = !   python not
"""

"""
#mantiqiy operatorlar 
x = 3
print (x < 10 and x > 2)
print (x < 10 or x > 2)
print ( not (x < 10 and x > 2))

"""
"""
  # aniqlash operatorlari
  
  # is bu funkitsiya xotirada egalagan ornini tekshiradi uzunligini ham
  # is   teng == vazifasini bajaradi
  # is not emas not
x = " olma " " banan "
y = " olma " " banan  "
print (x is y )
print (x is not  y )
"""


""""
#azolig operatorlari

# in bu  belgi x  ni ichidan y ni egalagan orni i qidiradi
# not in   bu ham  emas qaytaradi
x = " salom "" olam "
y=  " salom "
print (y in x  )  # qaytardi true
print (y not in   x  ) # qaytard false 
# endi tekarisini chiqaramiz
a = " salom " " java "
b= " java"
print (a in b ) # qaytardi false 
print (a not in   b ) # qaytardi true

"""

# bitli operatorlar


"""
# 2 bob malumot turlari bilan ishlash

# malumot turini aniqlashda biz type funkitsiyasidan foydalanamiz
x = -5.3
y = " salom "
print (type(x))
print (type(y))

x = ["olma " " banan" " nok "] # list 
print (type(x))
"""
# biz  malumot turlarini birdan bersak ham boladi
"""
x = str ( " java ")
print((x))
print(type(x))
"""

"""
# pytonda sonlar 3 xil turga bolinib kelar ekan
# int
# float
# complex
x=3j
y=3
a=5.5
print(type(x))
print(type(y))
print(type(a))

(12.00).is_integer()
x=complex(1,2)
print (x)
"""
"""
# random son aniqlaymiz
import random
print( random.randrange(1,100))
"""
"""
isimingizni_kiriting = input (" ismingizni kirting ")
familyangizni_kiriting= input (" familyangizni kirting  ")
yoshKiriting = input ( " yoshingizni kirting ")
qachon_tugulganingizni_kiriting= input (" qachon tugulganingizni kirting ")
boyingizni_kiriting = input(" boyingizni kirting ")
print ( isimingizni_kiriting)
print ( familyangizni_kiriting)
print ( yoshKiriting)
print ( qachon_tugulganingizni_kiriting)
print ( boyingizni_kiriting)
print (" tiplari ")
print (type( isimingizni_kiriting))
print (type ( familyangizni_kiriting))
print (type( yoshKiriting))
print (type( qachon_tugulganingizni_kiriting))
print (type( boyingizni_kiriting))
"""

"""
# bozordan non olish dasturini tuzmaiz

c=int(2000)
y=int (input("nechta non olishni kiriting "))
a=c*y
print ("sizga " ,a, " pul kerak")
"""
# if va elif shart operatorlari bilan ishlash
"""
a = int (input  (" a ni kiriting "))
b=int (input (" b ni kiriting "))
if a > b:
    print ("assalomu alekum")
elif a<b:
    print ("valekum assalom")
else:
    print ("hammasi yaxshi")

a=int (input ("a ni kiriting "))
b=int (input ("b ni kiriting "))
c = 0
for number in range(a,b):
    c=c+number
    print (number)
"""

"""
from  random import  randint
a  = randint(1,10)
b  = randint(1,10)
c= int (input('{} + {}  = '. format(a,b)))
if c == (a+b):
    print ("togri")
else:
    print ("xato")
"""

""""
from random import randint
a = randint(1,10)
c = 0;
if c == (a):
    print (" togri ")
else:
    print("xato")
"""

#dars 7  misol 4
""""
a=int(input(" a ni kirting "))
b=int(input(" b ni kirting "))
if a > 0 or b > 0 :
    print("  kamida biitasi katta 0 dan")
else:
    print(" ikalasiyam 0 dan mayd ")
"""
#dars 7 misol 1

"""
a = 5
print (not (a < 0 and a<5))

"""
#dars 7 mislo 2

"""
a = 5
print ( not (a<0 or a < 5 and 5 < 20),not ( a==0))
"""

"""
# dars 7  mislol 5
a = int ( input( " a soni ni kirting "))
b = int ( input( " b soni ni kirting "))
if a > 0 and b < 0 or a < 0 and b>0 :
    print (" ikkalasi ikkixil ishorali ")
else:
    print(" ishoralari teng ")
"""

""""
#dars 7 mislo 6

a=int (input(" a sonini kirting "))
if a%2==0:
    print ( " kiritilgan son juft son ")
else:
    print (" kiritilgan son juft emas toq son ")

"""

# dars  7  misol 7

""""
a= int(input(" a sonini kirting "))
if a >9 and a<100 and a%2==0:
    print ("ikki xonali juft son ")
elif a < 9 and a>0 and a%2==0:
    print ( " bir xonali juft son xato ")
elif a % 2==1:
    print (" bir xonali toq son ")
elif a >9 and a<100 and a%2==1:
    print (" iki xonali toq son ")
else:
    print (" manfiy son ")
"""

# dars  7  misol 8

"""
a = int (input(" a = "))
yuzlar  = int (a /100%10)
unlar = int (a /10%10)
birlar = int (a %10)
print(yuzlar)
print(unlar)
print(birlar)
if yuzlar ==unlar and yuzlar == birlar:
    print (" sonlar bir xil ")
elif yuzlar > unlar and unlar == birlar:
    print (" kamida 2 ta son teng ")
elif yuzlar > unlar or yuzlar > birlar and unlar>yuzlar or unlar > birlar and birlar> yuzlar or birlar >unlar:
    print(" sonlar harxil")
"""

# dars 7 mislo 9

""""
a= int (input( " a= "))
yuzlar = int (a/100%10)
unlar  = int (a/10%10)
birlar = int (a%10)
print(yuzlar)
print(unlar)
print(birlar)
if yuzlar==birlar:
    print (" chapdan oqigandayam ongdan oqigandayam birxil")
else:
    print (" xato")
"""
# dars 7  missol 10
"""""
x = int (input(" x = "))
y = int (input(" y = "))
if x - y == 27:
    print (" ortasidagi masofa teng ")
else:
    print("ortasidagi masofa  27  teng emas ")

"""
# dars 8 misol 2

""""
a= int (input ("a = "))
b= int (input ("b = "))
c =  int (input ("c = "))
print (max(a,b,c))
"""
 # dars  8 misol 2

"""
a = int (input(" a = "))
b = int (input(" b = "))
c = int (input(" c = "))
if  a > b and  a > c and  b > c:

      print (c,  b,a)

elif b > a and  b >c and  a > c :

    print ( c ,a ,  b)

elif  c > a and  c > b and b > a :
    print ( a, b , c)

elif a > b and  a < c and  c> b :

    print ( b , a ,c )

elif  a > b and  a > c and  b < c:

    print (b,c,a)

"""

# dars 8  misol  3

""""
a= int (input ( " a "))
if a == 0:
    print ("nol soni ",a )
elif a > 0 and a <10:
    print (" bir xonali musbat son ", a)
elif a > 9 and a<100:
    print (" ikki xonali musbat son ",a)
elif a > 99 and a <1000:
    print (" uch xonali musbat son ",a)
elif a < 0 and a >-10:
    print ( " bir xonali manfiy son ",a)
elif a <-9 and a>-100:
    print (" ikki xonali manfiy son ",a)
elif a<-99 and a >-1000:
    print ( " uch xonali manfiy son",a )
"""

# dars 8  mislol 4

"""
a = int ( input (" a = "))
if a > 0 and a < 10 and a%2==0:
    print (" bir xonali juft son ")
elif a > 0 and a < 9and a%2==1:
    print ( " bir xonali toq son ")
elif a > 9 and a < 100 and a%2==0 :
    print (" ikki xonali juft son ")
elif a > 9 and a< 100 and a%2==1:
    print (" ikki xonali toq son ")
elif a>99 and a<1000 and a%2 ==0:
    print (" uch xonali juft son ")
elif a> 99 and a <1000 and a %2 ==1:
    print (" uch xonali toq son ")
"""

# dars  8 misol 6

"""
a = int (input ( " talabani baxosini kirting =  "))
if a > 0 and a < 56:
    print (" 2 = qoniqarsiz ")
elif a > 55 and a <71:
    print ("  3 = qoniqarli ")
elif a > 70  and a <86:
    print ("  4 = yaxshi ")
elif a > 85  and a <101:
    print ("  5 = a'lo ")
"""

# dars 8  misol  7


""""
a = int ( input (" a = "))
yuzlar = int ( a/100%10)
onlar= int ( a/10%10)
birlar = int ( a%10)
print ( yuzlar )
print ( onlar  )
print ( birlar )

if yuzlar <onlar and onlar<birlar:
    print (" har tamondan oqiganda ham birxil ")
elif birlar < onlar and onlar <yuzlar:
    print (" har tamondan oqigandayam birxil ")
else:
    print (" xato")

"""

 # dars  8  misol 9

"""
a= int (input (" a =  "))
b= int (input (" b =  "))
c= int (input (" c =  "))
if a==b or a ==c or b==c:
    print  ( " kamida 2 tasi teng ")
else:
    print (" xato ")
"""

 # dars 8 misol 10

"""
energy = int ( input ( "  qolgan energiyani kiriting "))
dictance = int ( input ( "   distanc kiriting "))
perKilometr = 2.5
natija = float( dictance / perKilometr)
kerakquvat=int (energy - natija )
if natija > energy or natija==energy:
    print(" sizga quvat yetarli emas kerakli quvvat ", kerakquvat)
elif natija < energy or natija==energy:
    print (" sizning quvatingiz yetadi ortiqcha quvat bor =  ",kerakquvat)
"""
#dars 8 misol 11

"""
jarimatolovkuni = int (input (" kuni kirting "))
jarima = 10000
onfoyiz = int( jarima / 10 )
if jarimatolovkuni <= 3:
 print ( " tolash kerak bogan summa ", jarima-onfoyiz)
elif jarimatolovkuni >= 15:
 print (" tolash kerak bolgan summa ", jarima+onfoyiz)
else:
 print (" jarima tolash kerak bolgan summa",jarima)
"""
#dars 8  misol 12

"""
degree = int ( input( " enter the degree"))
if degree >=25:
 print ( " open the windoow it is too hot here ")
else:
 print (" clothe the windoow it is too colld here")

"""

#dars 8  mislol 13


"""
enterThcollor = str(input (" enter the collor "))
if enterThcollor=='red':
 print (" stop drive")
elif enterThcollor=='yellow':
 print ("preper to drive ")
elif enterThcollor == 'green':
 print (" drive ")
else:
 print ( " there are not like kinde of collor ")
"""

# dars 8  misol 14

""""
a= int (input (" a "))
b= int (input (" b "))
c= int (input (" c "))
print (" big  ", max (a,b,c))
print (" smoll", min (a,b,c))
"""

# dars 8  misol 15

"""
salery =int (input (" enter the sallary of the worker  "))
minimumWage =10000
if salery <= 5 * minimumWage:
    print (" should pay tax  ",float(salery/10))
elif salery >=5*minimumWage and salery<10*minimumWage:
    print ( " should pay tax ", float (salery/16))
elif salery>=10*minimumWage:
    print(" should pay tax ", float(salery/23))
"""

#dars  8  misol 16

"""
call= str (input(" enter the number which you want to call "))
if call == '101':
    print ( " you are calling to the fire srevice ")
elif call=='102':
    print (" you are calling tho the police service ")
elif call == '103':
    print (" you ar calling to the amergency medical assistance")
elif call == '104':
    print (" you ar callint to the natural gas service ")

"""
 # dars 8  misol 17

""""

parol = int ( input( " enter the parol "))

if parol == 111:
    print (" pasword is correct ")
else:
    print( " the paswor is incorrect ")
    
"""
# dars 8  misol 18
"""
lotery = int (input (" enter your lottery cod"))
lotery1 = int (input (" enter your lottery cod"))
lotery2= int (input (" enter your lottery cod"))
if   lotery==lotery2 and  lotery2==lotery1 and lotery == lotery1 :
    print ( " you winn 20 ")
elif lotery == lotery1 or lotery2 == lotery1 or lotery == lotery2:
    print (  " you win 10 ")
else:
    print (" you win  0 ")

"""
# dars misol 19
""""
energy = int ( input ( " enter the energy that your car have  "))
if energy < 21 :
    print (" you should charge the car ")
elif energy >20 and energy < 41 :
    print ( " you should charge your car  ")
elif energy >40 and energy <=  70:
    print ( " you hava enouth power ")

"""
   # we uae for loop  operators
""""
mehmonlar  = list( ["javoxir" ,"begzod ","java","akmal"])
for mehmon in mehmonlar:
    print (" you are welcom ", mehmon)
"""""
"""""
gustes = list (["javoxir ","java","ilxom"])
for gust in gustes:
    print (F" dear {gust}, we are happy to see you in our country ") # INSIDE THE PRINT WE USE  (F"..... { GUST },
    print(" the family of JA ")
"""""

"""
numbers = list (range (1,11))
for number in numbers:
    print (f"{number}, kvadirat of numbers {number**2},and the result  ")
"""
"""
numbers= list (range (1,11))
kvadirat_Numbers = []
for number in numbers:
    kvadirat_Numbers.append(number**2)

print (numbers)
print (kvadirat_Numbers)
"""

""""
firends = []
for firend in range(5):
    firends.append(input(f" { firend+1}, enter your best firends name "))
    
print (f"{ firends} your best firend ")


text = "emojie 😂 ⚓ "
print (text)

print ("hello \nworld")
print ("hello \tworld")
"""