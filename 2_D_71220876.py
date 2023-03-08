def hitung_mobil():
    tot_mobil = {k: 0 for k in ['Solo', 'Surabaya', 'Jogja', 'Magelang']} #tot_mobil = jumlah mobil
    
    while True:
        fromm = input("Masukkan asal mobil (ketik 'done' jika selesai): ").capitalize() #fromm = asal mobil
        
        if fromm == 'Done':
            break
        
        if fromm in tot_mobil:
            tot_mobil[fromm] += 1
        else:
            print(" ")
    
    for cityy, tot in tot_mobil.items():
        print("Jumlah mobil dari {}: {}".format(cityy, tot))

hitung_mobil()