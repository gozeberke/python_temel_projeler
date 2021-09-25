'''
sehirler=['İstanbul','Sivas']
plakalar=[34,58]
print(plakalar[sehirler.index('Sivas')])

plakalar={'Sivas ':58,'İstanbul':34}
print(plakalar['Sivas '])
'''
users={
    'berke göze': {
        'age':23,
        'email':'gozeberke@gmail.com',
        'phone':'5071176879'
    },
    'kerem efe göze': {
        'age':13,
        'email':'gozeefe@gmail.com',
        'phone':'5071176879'
    }

}
print(users['berke göze']['age'])