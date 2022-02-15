
"""
string1="Mehmet 1994 yılında doğdu"
print(string1, end=" ")
# "print" fonksiyonun "end" parametresiyle kullanılması
print("www", "akifgungor", "com",sep=".")
print(*"akifgungor",sep=".")
# "print" fonksiyonun "sep" parametresiyle kullanılması

#Tuple : Farklı veri türlerinin bir araya gelerek oluşturduğu veri türleridir;
tuple1 =(3,4.5,"Hello World",(4,6,3),'a')
tuple2 ="3,4.5,'Hello World',(4,6,3),'a' "
print(tuple1[2],tuple1[3],end="\n")
print(tuple2[4])

#List : Listeler de Tuple gibi farklı veri türlerinin bir araya gelmesiyle oluşmuştur. Farkı "list"te ekleme, çıkarma ve değiştirme işlemleri yapılabilir.
List_1=[4,3,5.25,"Ayşe",'a',[2,6,4.5]]
print(List_1[1])


#Dictionary: Sözlükler süslü parantezler ile ifade edilir ve  iki kısımdan oluşur; keys(anahtar) ve value(değer),  value kısmı bütün veri türünü içerebilir fakat keys kısmı sadece string ve int tipinde olabilir.

Dict_iller ={1:"Ankara",2:"İstanbul",3:"İzmir"}
print(type(Dict_iller))

isim = input("İsminizi Giriniz :")
print(isim)


# "input" fonksiyonu

sayi1 = int(23) #int(input("Birinci sayıyı girin :"))
sayi2 = int(33) #int(input("İkinci sayıyı girin :"))
 
topla = (sayi1+sayi2)
print(type(topla))
print("Toplam :",topla)

# "print" fonksiyonu "format" metodu.
isim="Mehmet"
yas=33
print("Merhaba {} Bey, yaşınız {}, hala çok gençsiniz...".format(isim,yas))


# "if" Deyimi

a=3
b=4
if a>=b:
    print("a b'den büyüktür.")
elif a<=b:
    print("a ile b birbirine eşit değildir")
else:
    print("a ile b birbirine eşit değildir")

# "while" Döngüsü
sayi=0
while sayi <=10:
    print(sayi,end=" ")
    sayi = sayi+1
print()

# "for" döngüsü
for sayı in range(0,11):
    print(sayı, end=" ")
print()

"""
"""
for harf in "Python":

    print(harf, end=" ")
    print()



# "len()" fonksiyonu
metin ="Python"
print(len(metin))


kullanici_adim="Python"
 
parolam ="1234"
 
giris_hakki=3


#break and continue
#*** break döngüden çıkar
#*** continue döngünün başına gider

while giris_hakki>0:
    giris_hakki -=1
    kullanici_adi = input("Kullanıcı Adınızı Girin :")
    parola = input("Parolayı Giriniz :")
 
    if kullanici_adi==kullanici_adim and parola== parolam:
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
        break
    else:
        print("Kullanıcı bilgileri yanlış tekrar deneyin!")

for sayi in range(20):
    if sayi%2==0:
        continue
    else:
        print(sayi)


liste =[2,"Python",5.4,[5,3],("Java",5,'a')]

print("liste",liste)
print (liste[2])
print (liste[4][0])
print (liste[0:2])
print ("[0:5:2],Liste[başlangıç,bitiş,artış miktarı]",liste[0:5:2])

print ("list'in metodlarını görme:dir(list)",dir(list))

meyveler=['elma', 'armut', 'kiraz', 'karpuz', 'Üzüm', 'portakal', 'armut']
meyveler.pop()

sayilar ={"1":"bir","2":"iki","3":"üç","4":"dört","5":"beş"}
 
print(sayilar.setdefault("4"),)
print(sayilar.setdefault("4","sekiz"),)

print(dir(dict))



#KÜMELER

kume = set()
kume= {"Python",'c',4,"Cahit"}
print(kume,type(kume))

kume ={1,2,3,4,5}
kume.add(6)
print(kume)

kume ={1,2,3,4,5,6}
kume_yedek =set()
kume_yedek=kume.copy()
print(kume_yedek)

kume ={1,2,3,4,5,6}
kume_2={7,8,9,10}
kume.update(kume_2)
print(kume)

A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {4,7,8,9,10}
print(type(A),type(B),type(C))
print(A.union(B.union(C)))
print(A.intersection(B))


import string
print(dir(string))

metin ="akifgungor.com python calismalari"
print(metin.capitalize())
print(metin.title())
print(metin.count("o"))
print(metin.upper())
print(metin.title().swapcase())
print(metin.center(45))
print(metin.replace("o","x"))
print("*".join(metin))

diller=["Python","Java","Ruby","C#"]
print(diller)
print(",".join(diller))

diller="Python,Java,Ruby,C#,aou,uoa"
print(diller.split("o"))


# Error, Bug, Exception
try:

    sayi1 = int(input("Bölünecek Sayıyı :"))
    sayi2 = int(input("Bölecek Sayıyı :"))

    sonuc = sayi1/sayi2
    print("Sonuc :",sonuc)

except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz lütfen sıfır dışında bir sayı girin")
except ValueError:
    print("Lütfen sayısal bir karakter girin..")
except:
    print("Beklenmeyen bir hata oluştu")

#try:
 
    sayi1 = int(input("Birinci Sayı :"))
    sayi2 = int(input("İkinci Sayı :"))
    sonuc = sayi1/sayi2
    print("Sonuc :",sonuc)
 
#except ZeroDivisionError  as acıklama:
  #  print(acıklama)

yari_cap = int(input("Yarıçapı girin :"))
pi=3.14
if yari_cap <= 0:
    raise ValueError("Yarıçap sıfır ve sıfırdan küçük bir değer olamaz")

sonuc =pi*(yari_cap**2)
print("Alan :{}'dir".format(sonuc))


#Dosya İşlemleri
import os
print(os.getcwd())

dosya = open("deneme.txt","a+")
dosya.write("Merhaba Millet :)")
dosya.close()

with open("deneme.txt","a+") as dosya:
    dosya.write("Merhaba Millet :)")

with open("deneme.txt","a+") as dosya:
    dosya.writelines(["Merhaba Millet\n","Python Derslerine Hosgeldiniz"])

print()

if os.path.isfile("deneme.txt"):
  with open("deneme.txt") as dosya:
    dosya.seek(10)
    print(dosya.read())

else:
    print("dosya bulunamadı")

os.remove("deneme.txt")
"""

def yazdir():
    print("akifgungor.com Python Örnekleri")

yazdir()

def yazdir():
    return "akifgungor.com Python Dersleri"

print(yazdir())

def toplama(sayi1,sayi2):
    return sayi1+sayi2

print("Sonuç :",toplama(3,4))

def toplama(sayi1=6,sayi2=8):
    return sayi1+sayi2x

print("Sonuç :",toplama(4,3))
