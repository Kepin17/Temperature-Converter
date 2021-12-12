# Converter Suhu

print(10*"=","Converter Suhu","="*10)

print("Kamu mau mngubah satuan apa?\n1) Celcius\n2) Reamur\n3) Fareheit\n4) Kelvin\n")
satuan = str(input("Masukan Satuan Suhu yang ingin diubah : "))

print("Permintaan diproses.....\n")

if satuan=="Celcius":
        num_C = float(input("Masukan angka :  "))
        print(10*"=","Masukan suhu yang kamu inginkan","="*10)
        unit = str(input("Masukan Satuan : "))

        if unit=="Reamur":
              resault = (4/5) * num_C
              print(f"\nHasil dari converter {satuan} ke {unit} = {resault} °R")

        elif unit=="Farenheit":
              resault = (9/5) * num_C + 32 
              print(f"\nHasil dari converter {satuan} ke {unit} = {resault} °F")
                   
        elif unit=="Kelvin":
              resault = ( num_C + 273 ) 
              print(f"\nHasil dari converter {satuan} ke {unit} = {resault} °K")
              
        else:
              print("Maaf,Satuan yang kamu masukan salah.Silahkan periksa kembali!")

elif satuan=="Reamur":
        num_R = float(input("Masukan angka :"))
        print(10*"=","Masukan suhu yang kamu inginkan","="*10)
        unit2 = str(input("Masukan Satuan : "))
        
        if unit2=="Celcius":
              resault = (5/4) * num_R
              print(f"\nHasil dari converter {satuan} ke {unit2} = {resault} °C")
        elif unit2=="Farenheit":
              resault = (9/4) * num_R + 32
              print(f"\nHasil dari converter {satuan} ke {unit2} = {resault} °C")
        
        elif unit2=="Kelvin":
              resault = (5/4) * num_R + 273
              print(f"\nHasil dari converter {satuan} ke {unit2} = {resault} °C")
       
        else:
              print("Maaf,Satuan yang kamu masukan salah.Silahkan periksa kembali!")

elif satuan=="Farenheit":
        num_F = float(input("Masukan angka :"))
        print(10*"=","Masukan suhu yang kamu inginkan","="*10)
        unit3 = str(input("Masukan Satuan : "))
        
        if unit3=="Celcius":
              resault = (5/9) * num_F - 32
              print(f"\nHasil dari converter {satuan} ke {unit3} = {resault} °C")
        elif unit3=="Reamur":
              resault = (4/9) * num_F - 32
              print(f"\nHasil dari converter {satuan} ke {unit3} = {resault} °C")
        
        elif unit3=="Kelvin":
              resault = 5/9 * (num_F - 32) + 273
              print(f"\nHasil dari converter {satuan} ke {unit3} = {resault} °C")
       
        else:
              print("Maaf,Satuan yang kamu masukan salah.Silahkan periksa kembali!")

        
elif satuan=="Kelvin":
        num_K = float(input("Masukan angka :"))
        print(10*"=","Masukan suhu yang kamu inginkan","="*10)
        unit4 = str(input("Masukan Satuan : "))
        
        if unit4=="Celcius":
              resault = num_K - 273
              print(f"\nHasil dari converter {satuan} ke {unit4} = {resault} °C")
        elif unit4=="Reamur":
              resault = 4 / 5 * ( num_K - 32 )
              print(f"\nHasil dari converter {satuan} ke {unit4} = {resault} °C")
        
        elif unit4=="Farenheit":
              resault = (num_K - 273.15 ) * 9/5 + 32
              print(f"\nHasil dari converter {satuan} ke {unit4} = {resault} °C")
       
        else:
              print("Maaf,Satuan yang kamu masukan salah.Silahkan periksa kembali!")

        
else:
        print("Maaf,Satuan yang kamu masukan salah.Silahkan periksa kembali!")

print("Akhir dari Pemograman")      