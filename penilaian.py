#cihuyyyyyy

tugas = 20
uts = 40
uas = 50

total = 0.3*tugas+0.3*uts+0.3*uas+10
nilaiHuruf = ''

if total>=80 and total<=100:
    nilaiHuruf='A'
elif total >=70 and total<=79:
    nilaiHuruf='A-'
elif total>=65 and total<=69:
    nilaiHuruf='B+'
elif total>=62 and total<=64:
    nilaiHuruf = 'B'
elif total>=55 and total<=61:
    nilaiHuruf='B-'
elif total>=50 and total <55:
    nilaiHuruf='C'
elif total>10 and total<50:
    nilaiHuruf='D'
elif total>=0 and total<=10:
    nilaiHuruf='E'

print (nilaiHuruf)
print (total)
    
    
