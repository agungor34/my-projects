

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

""" Dictionary: Sözlükler süslü parantezler ile ifade edilir ve  iki kısımdan oluşur; keys(anahtar) ve value(değer),  value kısmı bütün veri türünü içerebilir fakat keys kısmı sadece string ve int tipinde olabilir."""

Dict_iller ={1:"Ankara",2:"İstanbul",3:"İzmir"}

"""
isim = input("İsminizi Giriniz :")
print(isim)
"""


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
for harf in "Python": {
    print(harf, end=" ")
    print()
}
"""

# "len()" fonksiyonu
metin ="Python"
print(len(metin))


kullanici_adim="Python"
 
parolam ="1234"
 
giris_hakki=3

"""
break and continue
*** break döngüden çıkar
*** continue döngünün başına gider

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
"""

