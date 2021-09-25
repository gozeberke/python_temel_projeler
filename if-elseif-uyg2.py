'''
sayi=int(input('Bir sayi giriniz :'))
if sayi>100:
    print(f'Girdiğiniz sayı {sayi}: 100 den büyüktür.')
elif sayi<0:
    print(f'Girdiğiniz sayı {sayi}: 0 dan küçüktür.')
else:
    print(f'Girdğiniz sayı{sayi}: 0 ile 100 arasındadır.')
'''
sayi=int(input('Bir sayi giriniz: '))
if sayi%2==0:
    print('Girdiğiniz sayı çift sayıdır.')
else:
    print('Girdiğiniz sayı tek sayıdır.')