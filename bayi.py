baby = int(input("Berapa umur anda: "))

if baby <=2 :
    panggilan = ("bayi")
elif baby <=5 :
    panggilan = ("Balita")
elif baby <=12 :
    panggilan = ("Anak - Anak")
elif baby <=17 :
    panggilan = ("Remaja")
elif baby > 17 and baby <=30 :
    panggilan = ("Dewasa")
else :
    panggilan = ("Orang Tua")
print("Panggilan untuk manusia berumur", baby, "tahun adalah", panggilan)

