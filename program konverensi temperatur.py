import os

while True:
    try :
        print("\nPROGRAM KONVERENSI TEMPERATUR\n")

        celcius = float(input("Masukan Suhu : "))
        print(f"Suhu dalam celcius : {celcius}")

        fahrenhait = (9 / 5) * celcius + 32
        print(f"Suhu dalam fahrenhait : {fahrenhait}")

        reamur = (4 / 5) * celcius
        print(f"Suhu dalam reamur : {reamur}")

        kelvin = celcius + 273
        print(f"Suhu dalam kelvin : {kelvin}")
    except Exception as e :
        print("anda salah menginputkan :", e)
        
    ulang = input("Mau coba lagi? y/n : ").lower()
    if ulang != 'y':
        print("Program selesai!")
        break
    os.system('cls')