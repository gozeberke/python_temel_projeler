BerkeHesap={
    'ad':'Berke Göze',
    'hesapNo':'123456789',
    'bakiye':3000,
    'ekHesap':2000
}

EfeHesap={
    'ad':'Kerem Efe Göze',
    'hesapNo':'124356789',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye']+hesap['ekHesap']    

        if(toplam >= miktar):
            ekHesapKullanimi=input('Ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi=='e':
                
                ekhesapKulMik=miktar-hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap'] -=ekhesapKulMik
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınız da {hesap['bakiye']} bulunmaktadır.")    
        else:
            print('Yetersiz bakiye.') 
            bakiyeSorgula(hesap)       

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']}nolu hesabınızda {hesap['bakiye']} TL bulunamktadır. Ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")
paraCek(BerkeHesap,3000)
bakiyeSorgula(BerkeHesap)
print('************')
paraCek(BerkeHesap,2000)
bakiyeSorgula(BerkeHesap)
