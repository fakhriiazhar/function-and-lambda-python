#function with return value
def cek_genap_ganjil(n):
    if n % 2 == 0:
        return "ini adalah bilangan genap"
    else:
        return "ini adalah bilangan ganjil"
    
bilangan = int(input("Masukan bilangan: "))

hasil = cek_genap_ganjil(bilangan)
print(hasil)
