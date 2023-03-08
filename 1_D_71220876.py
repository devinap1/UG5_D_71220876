def ganti_kata(word, find, replace):
    kalimat_menjadi_list = word.split() 
    
    for i in range(len(kalimat_menjadi_list)):    # Looping untuk mengganti kata yang dicari dengan kata pengganti
        if kalimat_menjadi_list[i] == find:
            kalimat_menjadi_list[i] = replace
    new_word = " ".join(kalimat_menjadi_list)   
    return new_word   
word = input("masukkan kalimat: ") 
find = input("kata yang ingin diganti: ")
replace = input("diganti jadi: ")
new_word = ganti_kata(word, find, replace) 


print("kalimat batu : ", new_word) 