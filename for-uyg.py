sayilar= [1,3,5,7,9,12,19,21]

'''
for i in sayilar:
    if i%3==0:
        print(i)
'''
'''
toplam=0
for top in sayilar:
    toplam=toplam+top

print(toplam)
'''
'''
for tek in sayilar:
    if tek%2==1:
        tek=tek**2
        print(tek)
'''
'''
sehirler =['kocaeli','istanbul','ankara','sivas','denizli']

for n in sehirler:
        if (len(n) <= 5 ): #karakter uzunluğunu alıyor
            print(n)
   
'''
urunler=[
    {'name' : 'samsung S6','price': '3000'},
    {'name' : 'samsung S7','price': '4000'},
    {'name' : 'samsung S8','price': '5000'},
    {'name' : 'samsung S9','price': '6000'},
    {'name' : 'samsung S10','price': '7000'}
]
'''
toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat
print(toplam)
'''
for i in urunler:
    if int(i['price'])<=5000:
        print(i['name'])