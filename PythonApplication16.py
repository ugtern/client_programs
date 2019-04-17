import csv

def shifrator():
    a = str(input())

    a_shif = a.replace('L', '8+2')

    f = open('pass.txt', 'a')
    f.write(a_shif)
    f.close()

    print('complite')

def deshifrator():
    f = open('pass.txt', 'a')
    f2 = open('pass_deshif.txt', 'a')

    
    print(f)

    f.close()
    f2.close()



deshifrator()