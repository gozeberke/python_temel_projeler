isim = input('İsminiz : ')
yas=int(input('Yaşınız: '))
egitim=input('egitim durumu: ')

if (yas>=18) :
    if (egitim=='lise' or egitim=='lisans'):
         print(f'{isim} ehliyet alabilirsin.')
    else :
        print(f'{isim} m Egitim durumundan ötürü alamazsın bro:((')
else:
    print('Yasından dolayı ehliyet alamazsın bır :(((')