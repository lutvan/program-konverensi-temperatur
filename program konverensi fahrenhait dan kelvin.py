import os

while True:
    def konverensi_fahrenhaitTokelvin():
        input_fahrenhait = float(input("Masukan angka yang akan dikenverensi : "))
        kelvin = (input_fahrenhait - 32) * 5 / 9 + 273.15
        print(f"Berikut hasil konverensi farenhait ke kelvin : {kelvin}")


    def konverensi_kelvinTofahrenhait():
        input_kelvin = float(input("Masukan angka yang akan dikenverensi : "))
        fahrenhait = (input_kelvin - 273.15) * 9 / 5 + 32
        print(f"Berikut hasil konverensi kelvin ke fahrenhait : {fahrenhait}")

    print("\n PROGRAM KONVERENSI FAHRENHAIT DAN KELVIN\n")
    print(
        """
        1. Konverensi fahrenhait ke kelvin
        2. Konverensi kelvin ke fahrenhait
        """
    )
    chooice = int(input("Masukan pilihan anda : "))
    if chooice == 1:
        konverensi_fahrenhaitTokelvin()
    elif chooice == 2:
        konverensi_kelvinTofahrenhait()

    input_chooice = input("Mau coba lagi? y/n : ").lower()
    if input_chooice != 'y':
        print("Terimakasih telah mencoba")
        break

    os.system('cls')
