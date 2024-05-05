import pandas as pd
import numpy as np
from tabulate import tabulate

print("\nDELA PUSPITA LASMININGRUM / 22081010209\n")
print("STATISTIK KOMPUTASI (E-081)\n\n")

print("PREDIKSI KEPUASAN PEMBELAJARAN DARING MENGGUNAKAN ALGORITMA NAIVE BAYES\n")
print("=======================================================================\n")
print("terdapat variabel dari A1 sampai A11 yang berisi pertanyaan-pertanyaan kuisioner\n")
print("terdapat 5 value untuk diisi sb(sangat baik), b(baik), c(cukup), k(kurang), sk(sangat kurang)\n")
print("hasil prediksi dibedakan jadi 2 kelas Puas dan Tpuas(Tidak Puas)\n")

# Membaca file excel
path = r'C:\Users\dela puspita\Documents\INFORMATIKA SMT 3\STATISTIK KOMPUTASI\data_naivebayes.xlsx'
df = pd.read_excel(path)

# Membaca kolom 'Hasil'
kolom_hasil = df['Hasil']

# Menghitung jumlah absolut Tpuas dan Puas dalam kolom 'Hasil'
jumlah_Tpuas = (df['Hasil'] == 'Tpuas').sum()/100
jumlah_Puas = (df['Hasil'] == 'Puas').sum()/100

print(f"Jumlah Tpuas: {jumlah_Tpuas}")
print(f"Jumlah Puas: {jumlah_Puas}")

# KOLOM A1
prob_A1 = df['A1'].head(81).value_counts()
print(prob_A1)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A1 = data_naivebayes["A1"]

# Jumlah Kejadian berdasarkan Hasil Tpuas (Tidak Puas) kolom A1
count_A1_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A1_b_Tpuas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A1_c_Tpuas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A1_k_Tpuas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A1_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A1_Tpuas = count_A1_sb_Tpuas + \
    count_A1_b_Tpuas+count_A1_c_Tpuas + count_A1_k_Tpuas + count_A1_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A1
count_A1_sb_Puas = data_naivebayes.loc[data_naivebayes['A1']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A1_b_Puas = data_naivebayes.loc[data_naivebayes['A1']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A1_c_Puas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A1_k_Puas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A1_sk_Puas = data_naivebayes.loc[data_naivebayes['A1']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A1_Puas = count_A1_sb_Puas + \
    count_A1_b_Puas+count_A1_c_Puas+count_A1_k_Puas+count_A1_sk_Puas

# probabilitas Tpuas kolom A1
prob_count_A1_sb_Tpuas = count_A1_sb_Tpuas / \
    total_A1_Tpuas
prob_count_A1_b_Tpuas = count_A1_b_Tpuas / \
    total_A1_Tpuas
prob_count_A1_c_Tpuas = count_A1_c_Tpuas / \
    total_A1_Tpuas
prob_count_A1_k_Tpuas = count_A1_k_Tpuas / \
    total_A1_Tpuas
prob_count_A1_sk_Tpuas = count_A1_sk_Tpuas / \
    total_A1_Tpuas  
total_Tpuas = prob_count_A1_sb_Tpuas + \
    prob_count_A1_b_Tpuas + prob_count_A1_c_Tpuas+prob_count_A1_k_Tpuas+prob_count_A1_sk_Tpuas 
    
    
# probabilitas Puas kolom A1
prob_count_A1_sb_Puas = count_A1_sb_Puas / \
    total_A1_Puas
prob_count_A1_b_Puas = count_A1_b_Puas / \
    total_A1_Puas
prob_count_A1_c_Puas = count_A1_c_Puas / \
    total_A1_Puas
prob_count_A1_k_Puas = count_A1_k_Puas / \
    total_A1_Puas
prob_count_A1_sk_Puas = count_A1_sk_Puas / \
    total_A1_Puas
total_Puas = prob_count_A1_sb_Puas + \
    prob_count_A1_b_Puas + prob_count_A1_c_Puas+prob_count_A1_k_Puas+prob_count_A1_sk_Puas

# Menyusun data untuk tabel kolom A1
data_table = [
    ["sb", count_A1_sb_Tpuas, count_A1_sb_Puas, round(
        prob_count_A1_sb_Tpuas, 2), round(prob_count_A1_sb_Puas, 2)],
    ["b", count_A1_b_Tpuas, count_A1_b_Puas, round(
        prob_count_A1_b_Tpuas, 2), round(prob_count_A1_b_Puas, 2)],
    ["c", count_A1_c_Tpuas, count_A1_c_Puas, round(
        prob_count_A1_c_Tpuas, 2), round(prob_count_A1_c_Puas, 2)],
    ["k", count_A1_k_Tpuas, count_A1_k_Puas, round(
        prob_count_A1_k_Tpuas, 2), round(prob_count_A1_k_Puas, 2)],
    ["sk", count_A1_sk_Tpuas, count_A1_sk_Puas, round(
        prob_count_A1_sk_Tpuas, 2), round(prob_count_A1_sk_Puas, 2)],
    ["Total", total_A1_Tpuas, total_A1_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A1
table_headers = ["A1", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A2
prob_A2 = df['A2'].head(81).value_counts()
print(prob_A2)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A2 = data_naivebayes["A2"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A2
count_A2_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A2']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A2_b_Tpuas = data_naivebayes.loc[data_naivebayes['A2']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A2_c_Tpuas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A2_k_Tpuas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A2_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A2_Tpuas = count_A2_sb_Tpuas + \
    count_A2_b_Tpuas+count_A2_c_Tpuas + count_A2_k_Tpuas + count_A2_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A2
count_A2_sb_Puas = data_naivebayes.loc[data_naivebayes['A2']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A2_b_Puas = data_naivebayes.loc[data_naivebayes['A2']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A2_c_Puas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A2_k_Puas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A2_sk_Puas = data_naivebayes.loc[data_naivebayes['A2']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A2_Puas = count_A2_sb_Puas + \
    count_A2_b_Puas+count_A2_c_Puas+count_A2_k_Puas+count_A2_sk_Puas

# probabilitas Tpuas kolom A2
prob_count_A2_sb_Tpuas = count_A2_sb_Tpuas / \
    total_A2_Tpuas
prob_count_A2_b_Tpuas = count_A2_b_Tpuas / \
    total_A2_Tpuas
prob_count_A2_c_Tpuas = count_A2_c_Tpuas / \
    total_A2_Tpuas
prob_count_A2_k_Tpuas = count_A2_k_Tpuas / \
    total_A2_Tpuas
prob_count_A2_sk_Tpuas = count_A2_sk_Tpuas / \
    total_A2_Tpuas  
total_Tpuas = prob_count_A2_sb_Tpuas + \
    prob_count_A2_b_Tpuas + prob_count_A2_c_Tpuas+prob_count_A2_k_Tpuas+prob_count_A2_sk_Tpuas

# probabilitas Puas kolom A2
prob_count_A2_sb_Puas = count_A2_sb_Puas / \
    total_A2_Puas
prob_count_A2_b_Puas = count_A2_b_Puas / \
    total_A2_Puas
prob_count_A2_c_Puas = count_A2_c_Puas / \
    total_A2_Puas
prob_count_A2_k_Puas = count_A2_k_Puas / \
    total_A2_Puas
prob_count_A2_sk_Puas = count_A2_sk_Puas / \
    total_A2_Puas
total_Puas = prob_count_A2_sb_Puas + \
    prob_count_A2_b_Puas + prob_count_A2_c_Puas+prob_count_A2_k_Puas+prob_count_A2_sk_Puas

# Menyusun data untuk tabel kolom A2
data_table = [
    ["sb", count_A2_sb_Tpuas, count_A2_sb_Puas, round(
        prob_count_A2_sb_Tpuas, 2), round(prob_count_A2_sb_Puas, 2)],
    ["b", count_A2_b_Tpuas, count_A2_b_Puas, round(
        prob_count_A2_b_Tpuas, 2), round(prob_count_A2_b_Puas, 2)],
    ["c", count_A2_c_Tpuas, count_A2_c_Puas, round(
        prob_count_A2_c_Tpuas, 2), round(prob_count_A2_c_Puas, 2)],
    ["k", count_A2_k_Tpuas, count_A2_k_Puas, round(
        prob_count_A2_k_Tpuas, 2), round(prob_count_A2_k_Puas, 2)],
    ["sk", count_A2_sk_Tpuas, count_A2_sk_Puas, round(
        prob_count_A2_sk_Tpuas, 2), round(prob_count_A2_sk_Puas, 2)],
    ["Total", total_A2_Tpuas, total_A2_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A2
table_headers = ["A2", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A3
prob_A3 = df['A3'].head(81).value_counts()
print(prob_A3)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A3 = data_naivebayes["A3"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A3
count_A3_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A3']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A3_b_Tpuas = data_naivebayes.loc[data_naivebayes['A3']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A3_c_Tpuas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A3_k_Tpuas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A3_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A3_Tpuas = count_A3_sb_Tpuas + \
    count_A3_b_Tpuas+count_A3_c_Tpuas + count_A3_k_Tpuas + count_A3_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A3
count_A3_sb_Puas = data_naivebayes.loc[data_naivebayes['A3']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A3_b_Puas = data_naivebayes.loc[data_naivebayes['A3']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A3_c_Puas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A3_k_Puas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A3_sk_Puas = data_naivebayes.loc[data_naivebayes['A3']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A3_Puas = count_A3_sb_Puas + \
    count_A3_b_Puas+count_A3_c_Puas+count_A3_k_Puas+count_A3_sk_Puas

# probabilitas Tpuas kolom A3
prob_count_A3_sb_Tpuas = count_A3_sb_Tpuas / \
    total_A3_Tpuas
prob_count_A3_b_Tpuas = count_A3_b_Tpuas / \
    total_A3_Tpuas
prob_count_A3_c_Tpuas = count_A3_c_Tpuas / \
    total_A3_Tpuas
prob_count_A3_k_Tpuas = count_A3_k_Tpuas / \
    total_A3_Tpuas
prob_count_A3_sk_Tpuas = count_A3_sk_Tpuas / \
    total_A3_Tpuas  
total_Tpuas = prob_count_A3_sb_Tpuas + \
    prob_count_A3_b_Tpuas + prob_count_A3_c_Tpuas+prob_count_A3_k_Tpuas+prob_count_A3_sk_Tpuas

# probabilitas Puas kolom A3
prob_count_A3_sb_Puas = count_A3_sb_Puas / \
    total_A3_Puas
prob_count_A3_b_Puas = count_A3_b_Puas / \
    total_A3_Puas
prob_count_A3_c_Puas = count_A3_c_Puas / \
    total_A3_Puas
prob_count_A3_k_Puas = count_A3_k_Puas / \
    total_A3_Puas
prob_count_A3_sk_Puas = count_A3_sk_Puas / \
    total_A3_Puas
total_Puas = prob_count_A3_sb_Puas + \
    prob_count_A3_b_Puas + prob_count_A3_c_Puas+prob_count_A3_k_Puas+prob_count_A3_sk_Puas

# Menyusun data untuk tabel kolom A3
data_table = [
    ["sb", count_A3_sb_Tpuas, count_A3_sb_Puas, round(
        prob_count_A3_sb_Tpuas, 2), round(prob_count_A3_sb_Puas, 2)],
    ["b", count_A3_b_Tpuas, count_A3_b_Puas, round(
        prob_count_A3_b_Tpuas, 2), round(prob_count_A3_b_Puas, 2)],
    ["c", count_A3_c_Tpuas, count_A3_c_Puas, round(
        prob_count_A3_c_Tpuas, 2), round(prob_count_A3_c_Puas, 2)],
    ["k", count_A3_k_Tpuas, count_A3_k_Puas, round(
        prob_count_A3_k_Tpuas, 2), round(prob_count_A3_k_Puas, 2)],
    ["sk", count_A3_sk_Tpuas, count_A3_sk_Puas, round(
        prob_count_A3_sk_Tpuas, 2), round(prob_count_A3_sk_Puas, 2)],
    ["Total", total_A3_Tpuas, total_A3_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A3
table_headers = ["A3", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A4
prob_A4 = df['A4'].head(81).value_counts()
print(prob_A4)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A4 = data_naivebayes["A4"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A4
count_A4_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A4']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A4_b_Tpuas = data_naivebayes.loc[data_naivebayes['A4']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A4_c_Tpuas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A4_k_Tpuas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A4_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A4_Tpuas = count_A4_sb_Tpuas + \
    count_A4_b_Tpuas+count_A4_c_Tpuas + count_A4_k_Tpuas + count_A4_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A4
count_A4_sb_Puas = data_naivebayes.loc[data_naivebayes['A4']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A4_b_Puas = data_naivebayes.loc[data_naivebayes['A4']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A4_c_Puas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A4_k_Puas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A4_sk_Puas = data_naivebayes.loc[data_naivebayes['A4']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A4_Puas = count_A4_sb_Puas + \
    count_A4_b_Puas+count_A4_c_Puas+count_A4_k_Puas+count_A4_sk_Puas

# probabilitas Tpuas kolom A4
prob_count_A4_sb_Tpuas = count_A4_sb_Tpuas / \
    total_A4_Tpuas
prob_count_A4_b_Tpuas = count_A4_b_Tpuas / \
    total_A4_Tpuas
prob_count_A4_c_Tpuas = count_A4_c_Tpuas / \
    total_A4_Tpuas
prob_count_A4_k_Tpuas = count_A4_k_Tpuas / \
    total_A4_Tpuas
prob_count_A4_sk_Tpuas = count_A4_sk_Tpuas / \
    total_A4_Tpuas  
total_Tpuas = prob_count_A4_sb_Tpuas + \
    prob_count_A4_b_Tpuas + prob_count_A4_c_Tpuas+prob_count_A4_k_Tpuas+prob_count_A4_sk_Tpuas

# probabilitas Puas kolom A4
prob_count_A4_sb_Puas = count_A4_sb_Puas / \
    total_A4_Puas
prob_count_A4_b_Puas = count_A4_b_Puas / \
    total_A4_Puas
prob_count_A4_c_Puas = count_A4_c_Puas / \
    total_A4_Puas
prob_count_A4_k_Puas = count_A4_k_Puas / \
    total_A4_Puas
prob_count_A4_sk_Puas = count_A4_sk_Puas / \
    total_A4_Puas
total_Puas = prob_count_A4_sb_Puas + \
    prob_count_A4_b_Puas + prob_count_A4_c_Puas+prob_count_A4_k_Puas+prob_count_A4_sk_Puas

# Menyusun data untuk tabel kolom A4
data_table = [
    ["sb", count_A4_sb_Tpuas, count_A4_sb_Puas, round(
        prob_count_A4_sb_Tpuas, 2), round(prob_count_A4_sb_Puas, 2)],
    ["b", count_A4_b_Tpuas, count_A4_b_Puas, round(
        prob_count_A4_b_Tpuas, 2), round(prob_count_A4_b_Puas, 2)],
    ["c", count_A4_c_Tpuas, count_A4_c_Puas, round(
        prob_count_A4_c_Tpuas, 2), round(prob_count_A4_c_Puas, 2)],
    ["k", count_A4_k_Tpuas, count_A4_k_Puas, round(
        prob_count_A4_k_Tpuas, 2), round(prob_count_A4_k_Puas, 2)],
    ["sk", count_A4_sk_Tpuas, count_A4_sk_Puas, round(
        prob_count_A4_sk_Tpuas, 2), round(prob_count_A4_sk_Puas, 2)],
    ["Total", total_A4_Tpuas, total_A4_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A4
table_headers = ["A4", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A5
prob_A5 = df['A5'].head(81).value_counts()
print(prob_A5)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A5 = data_naivebayes["A5"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A5
count_A5_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A5']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A5_b_Tpuas = data_naivebayes.loc[data_naivebayes['A5']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A5_c_Tpuas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A5_k_Tpuas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A5_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A5_Tpuas = count_A5_sb_Tpuas + \
    count_A5_b_Tpuas+count_A5_c_Tpuas + count_A5_k_Tpuas + count_A5_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A5
count_A5_sb_Puas = data_naivebayes.loc[data_naivebayes['A5']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A5_b_Puas = data_naivebayes.loc[data_naivebayes['A5']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A5_c_Puas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A5_k_Puas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A5_sk_Puas = data_naivebayes.loc[data_naivebayes['A5']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A5_Puas = count_A5_sb_Puas + \
    count_A5_b_Puas+count_A5_c_Puas+count_A5_k_Puas+count_A5_sk_Puas

# probabilitas Tpuas kolom A5
prob_count_A5_sb_Tpuas = count_A5_sb_Tpuas / \
    total_A5_Tpuas
prob_count_A5_b_Tpuas = count_A5_b_Tpuas / \
    total_A5_Tpuas
prob_count_A5_c_Tpuas = count_A5_c_Tpuas / \
    total_A5_Tpuas
prob_count_A5_k_Tpuas = count_A5_k_Tpuas / \
    total_A5_Tpuas
prob_count_A5_sk_Tpuas = count_A5_sk_Tpuas / \
    total_A5_Tpuas  
total_Tpuas = prob_count_A5_sb_Tpuas + \
    prob_count_A5_b_Tpuas + prob_count_A5_c_Tpuas+prob_count_A5_k_Tpuas+prob_count_A5_sk_Tpuas

# probabilitas Puas kolom A5
prob_count_A5_sb_Puas = count_A5_sb_Puas / \
    total_A5_Puas
prob_count_A5_b_Puas = count_A5_b_Puas / \
    total_A5_Puas
prob_count_A5_c_Puas = count_A5_c_Puas / \
    total_A5_Puas
prob_count_A5_k_Puas = count_A5_k_Puas / \
    total_A5_Puas
prob_count_A5_sk_Puas = count_A5_sk_Puas / \
    total_A5_Puas
total_Puas = prob_count_A5_sb_Puas + \
    prob_count_A5_b_Puas + prob_count_A5_c_Puas+prob_count_A5_k_Puas+prob_count_A5_sk_Puas

# Menyusun data untuk tabel kolom A5
data_table = [
    ["sb", count_A5_sb_Tpuas, count_A5_sb_Puas, round(
        prob_count_A5_sb_Tpuas, 2), round(prob_count_A5_sb_Puas, 2)],
    ["b", count_A5_b_Tpuas, count_A5_b_Puas, round(
        prob_count_A5_b_Tpuas, 2), round(prob_count_A5_b_Puas, 2)],
    ["c", count_A5_c_Tpuas, count_A5_c_Puas, round(
        prob_count_A5_c_Tpuas, 2), round(prob_count_A5_c_Puas, 2)],
    ["k", count_A5_k_Tpuas, count_A5_k_Puas, round(
        prob_count_A5_k_Tpuas, 2), round(prob_count_A5_k_Puas, 2)],
    ["sk", count_A5_sk_Tpuas, count_A5_sk_Puas, round(
        prob_count_A5_sk_Tpuas, 2), round(prob_count_A5_sk_Puas, 2)],
    ["Total", total_A5_Tpuas, total_A5_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A5
table_headers = ["A5", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A6
prob_A6 = df['A6'].head(81).value_counts()
print(prob_A6)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A6 = data_naivebayes["A6"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A6
count_A6_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A6']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A6_b_Tpuas = data_naivebayes.loc[data_naivebayes['A6']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A6_c_Tpuas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A6_k_Tpuas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A6_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A6_Tpuas = count_A6_sb_Tpuas + \
    count_A6_b_Tpuas+count_A6_c_Tpuas + count_A6_k_Tpuas + count_A6_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A6
count_A6_sb_Puas = data_naivebayes.loc[data_naivebayes['A6']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A6_b_Puas = data_naivebayes.loc[data_naivebayes['A6']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A6_c_Puas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A6_k_Puas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A6_sk_Puas = data_naivebayes.loc[data_naivebayes['A6']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A6_Puas = count_A6_sb_Puas + \
    count_A6_b_Puas+count_A6_c_Puas+count_A6_k_Puas+count_A6_sk_Puas

# probabilitas Tpuas kolom A6
prob_count_A6_sb_Tpuas = count_A6_sb_Tpuas / \
    total_A6_Tpuas
prob_count_A6_b_Tpuas = count_A6_b_Tpuas / \
    total_A6_Tpuas
prob_count_A6_c_Tpuas = count_A6_c_Tpuas / \
    total_A6_Tpuas
prob_count_A6_k_Tpuas = count_A6_k_Tpuas / \
    total_A6_Tpuas
prob_count_A6_sk_Tpuas = count_A6_sk_Tpuas / \
    total_A6_Tpuas  
total_Tpuas = prob_count_A6_sb_Tpuas + \
    prob_count_A6_b_Tpuas + prob_count_A6_c_Tpuas+prob_count_A6_k_Tpuas+prob_count_A6_sk_Tpuas

# probabilitas Puas kolom A6
prob_count_A6_sb_Puas = count_A6_sb_Puas / \
    total_A6_Puas
prob_count_A6_b_Puas = count_A6_b_Puas / \
    total_A6_Puas
prob_count_A6_c_Puas = count_A6_c_Puas / \
    total_A6_Puas
prob_count_A6_k_Puas = count_A6_k_Puas / \
    total_A6_Puas
prob_count_A6_sk_Puas = count_A6_sk_Puas / \
    total_A6_Puas
total_Puas = prob_count_A6_sb_Puas + \
    prob_count_A6_b_Puas + prob_count_A6_c_Puas+prob_count_A6_k_Puas+prob_count_A6_sk_Puas

# Menyusun data untuk tabel kolom A6
data_table = [
    ["sb", count_A6_sb_Tpuas, count_A6_sb_Puas, round(
        prob_count_A6_sb_Tpuas, 2), round(prob_count_A6_sb_Puas, 2)],
    ["b", count_A6_b_Tpuas, count_A6_b_Puas, round(
        prob_count_A6_b_Tpuas, 2), round(prob_count_A6_b_Puas, 2)],
    ["c", count_A6_c_Tpuas, count_A6_c_Puas, round(
        prob_count_A6_c_Tpuas, 2), round(prob_count_A6_c_Puas, 2)],
    ["k", count_A6_k_Tpuas, count_A6_k_Puas, round(
        prob_count_A6_k_Tpuas, 2), round(prob_count_A6_k_Puas, 2)],
    ["sk", count_A6_sk_Tpuas, count_A6_sk_Puas, round(
        prob_count_A6_sk_Tpuas, 2), round(prob_count_A6_sk_Puas, 2)],
    ["Total", total_A6_Tpuas, total_A6_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A6
table_headers = ["A6", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A7
prob_A7 = df['A7'].head(81).value_counts()
print(prob_A7)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A7 = data_naivebayes["A7"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A7
count_A7_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A7']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A7_b_Tpuas = data_naivebayes.loc[data_naivebayes['A7']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A7_c_Tpuas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A7_k_Tpuas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A7_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A7_Tpuas = count_A7_sb_Tpuas + \
    count_A7_b_Tpuas+count_A7_c_Tpuas + count_A7_k_Tpuas + count_A7_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A7
count_A7_sb_Puas = data_naivebayes.loc[data_naivebayes['A7']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A7_b_Puas = data_naivebayes.loc[data_naivebayes['A7']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A7_c_Puas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A7_k_Puas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A7_sk_Puas = data_naivebayes.loc[data_naivebayes['A7']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A7_Puas = count_A7_sb_Puas + \
    count_A7_b_Puas+count_A7_c_Puas+count_A7_k_Puas+count_A7_sk_Puas

# probabilitas Tpuas kolom A7
prob_count_A7_sb_Tpuas = count_A7_sb_Tpuas / \
    total_A7_Tpuas
prob_count_A7_b_Tpuas = count_A7_b_Tpuas / \
    total_A7_Tpuas
prob_count_A7_c_Tpuas = count_A7_c_Tpuas / \
    total_A7_Tpuas
prob_count_A7_k_Tpuas = count_A7_k_Tpuas / \
    total_A7_Tpuas
prob_count_A7_sk_Tpuas = count_A7_sk_Tpuas / \
    total_A7_Tpuas  
total_Tpuas = prob_count_A7_sb_Tpuas + \
    prob_count_A7_b_Tpuas + prob_count_A7_c_Tpuas+prob_count_A7_k_Tpuas+prob_count_A7_sk_Tpuas

# probabilitas Puas kolom A7
prob_count_A7_sb_Puas = count_A7_sb_Puas / \
    total_A7_Puas
prob_count_A7_b_Puas = count_A7_b_Puas / \
    total_A7_Puas
prob_count_A7_c_Puas = count_A7_c_Puas / \
    total_A7_Puas
prob_count_A7_k_Puas = count_A7_k_Puas / \
    total_A7_Puas
prob_count_A7_sk_Puas = count_A7_sk_Puas / \
    total_A7_Puas
total_Puas = prob_count_A7_sb_Puas + \
    prob_count_A7_b_Puas + prob_count_A7_c_Puas+prob_count_A7_k_Puas+prob_count_A7_sk_Puas

# Menyusun data untuk tabel kolom A7
data_table = [
    ["sb", count_A7_sb_Tpuas, count_A7_sb_Puas, round(
        prob_count_A7_sb_Tpuas, 2), round(prob_count_A7_sb_Puas, 2)],
    ["b", count_A7_b_Tpuas, count_A7_b_Puas, round(
        prob_count_A7_b_Tpuas, 2), round(prob_count_A7_b_Puas, 2)],
    ["c", count_A7_c_Tpuas, count_A7_c_Puas, round(
        prob_count_A7_c_Tpuas, 2), round(prob_count_A7_c_Puas, 2)],
    ["k", count_A7_k_Tpuas, count_A7_k_Puas, round(
        prob_count_A7_k_Tpuas, 2), round(prob_count_A7_k_Puas, 2)],
    ["sk", count_A7_sk_Tpuas, count_A7_sk_Puas, round(
        prob_count_A7_sk_Tpuas, 2), round(prob_count_A7_sk_Puas, 2)],
    ["Total", total_A7_Tpuas, total_A7_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A7
table_headers = ["A7", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A8
prob_A8 = df['A8'].head(81).value_counts()
print(prob_A8)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A8 = data_naivebayes["A8"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A8
count_A8_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A8']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A8_b_Tpuas = data_naivebayes.loc[data_naivebayes['A8']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A8_c_Tpuas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A8_k_Tpuas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A8_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A8_Tpuas = count_A8_sb_Tpuas + \
    count_A8_b_Tpuas+count_A8_c_Tpuas + count_A8_k_Tpuas + count_A8_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A8
count_A8_sb_Puas = data_naivebayes.loc[data_naivebayes['A8']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A8_b_Puas = data_naivebayes.loc[data_naivebayes['A8']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A8_c_Puas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A8_k_Puas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A8_sk_Puas = data_naivebayes.loc[data_naivebayes['A8']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A8_Puas = count_A8_sb_Puas + \
    count_A8_b_Puas+count_A8_c_Puas+count_A8_k_Puas+count_A8_sk_Puas

# probabilitas Tpuas kolom A8
prob_count_A8_sb_Tpuas = count_A8_sb_Tpuas / \
    total_A8_Tpuas
prob_count_A8_b_Tpuas = count_A8_b_Tpuas / \
    total_A8_Tpuas
prob_count_A8_c_Tpuas = count_A8_c_Tpuas / \
    total_A8_Tpuas
prob_count_A8_k_Tpuas = count_A8_k_Tpuas / \
    total_A8_Tpuas
prob_count_A8_sk_Tpuas = count_A8_sk_Tpuas / \
    total_A8_Tpuas  
total_Tpuas = prob_count_A8_sb_Tpuas + \
    prob_count_A8_b_Tpuas + prob_count_A8_c_Tpuas+prob_count_A8_k_Tpuas+prob_count_A8_sk_Tpuas

# probabilitas Puas kolom A8
prob_count_A8_sb_Puas = count_A8_sb_Puas / \
    total_A8_Puas
prob_count_A8_b_Puas = count_A8_b_Puas / \
    total_A8_Puas
prob_count_A8_c_Puas = count_A8_c_Puas / \
    total_A8_Puas
prob_count_A8_k_Puas = count_A8_k_Puas / \
    total_A8_Puas
prob_count_A8_sk_Puas = count_A8_sk_Puas / \
    total_A8_Puas
total_Puas = prob_count_A8_sb_Puas + \
    prob_count_A8_b_Puas + prob_count_A8_c_Puas+prob_count_A8_k_Puas+prob_count_A8_sk_Puas

# Menyusun data untuk tabel kolom A8
data_table = [
    ["sb", count_A8_sb_Tpuas, count_A8_sb_Puas, round(
        prob_count_A8_sb_Tpuas, 2), round(prob_count_A8_sb_Puas, 2)],
    ["b", count_A8_b_Tpuas, count_A8_b_Puas, round(
        prob_count_A8_b_Tpuas, 2), round(prob_count_A8_b_Puas, 2)],
    ["c", count_A8_c_Tpuas, count_A8_c_Puas, round(
        prob_count_A8_c_Tpuas, 2), round(prob_count_A8_c_Puas, 2)],
    ["k", count_A8_k_Tpuas, count_A8_k_Puas, round(
        prob_count_A8_k_Tpuas, 2), round(prob_count_A8_k_Puas, 2)],
    ["sk", count_A8_sk_Tpuas, count_A8_sk_Puas, round(
        prob_count_A8_sk_Tpuas, 2), round(prob_count_A8_sk_Puas, 2)],
    ["Total", total_A8_Tpuas, total_A8_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A8
table_headers = ["A8", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A9
prob_A9 = df['A9'].head(81).value_counts()
print(prob_A9)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A9 = data_naivebayes["A9"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A9
count_A9_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A9']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A9_b_Tpuas = data_naivebayes.loc[data_naivebayes['A9']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A9_c_Tpuas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A9_k_Tpuas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A9_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A9_Tpuas = count_A9_sb_Tpuas + \
    count_A9_b_Tpuas+count_A9_c_Tpuas + count_A9_k_Tpuas + count_A9_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A9
count_A9_sb_Puas = data_naivebayes.loc[data_naivebayes['A9']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A9_b_Puas = data_naivebayes.loc[data_naivebayes['A9']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A9_c_Puas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A9_k_Puas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A9_sk_Puas = data_naivebayes.loc[data_naivebayes['A9']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A9_Puas = count_A9_sb_Puas + \
    count_A9_b_Puas+count_A9_c_Puas+count_A9_k_Puas+count_A9_sk_Puas

# probabilitas Tpuas kolom A9
prob_count_A9_sb_Tpuas = count_A9_sb_Tpuas / \
    total_A9_Tpuas
prob_count_A9_b_Tpuas = count_A9_b_Tpuas / \
    total_A9_Tpuas
prob_count_A9_c_Tpuas = count_A9_c_Tpuas / \
    total_A9_Tpuas
prob_count_A9_k_Tpuas = count_A9_k_Tpuas / \
    total_A9_Tpuas
prob_count_A9_sk_Tpuas = count_A9_sk_Tpuas / \
    total_A9_Tpuas  
total_Tpuas = prob_count_A9_sb_Tpuas + \
    prob_count_A9_b_Tpuas + prob_count_A9_c_Tpuas+prob_count_A9_k_Tpuas+prob_count_A9_sk_Tpuas

# probabilitas Puas kolom A9
prob_count_A9_sb_Puas = count_A9_sb_Puas / \
    total_A9_Puas
prob_count_A9_b_Puas = count_A9_b_Puas / \
    total_A9_Puas
prob_count_A9_c_Puas = count_A9_c_Puas / \
    total_A9_Puas
prob_count_A9_k_Puas = count_A9_k_Puas / \
    total_A9_Puas
prob_count_A9_sk_Puas = count_A9_sk_Puas / \
    total_A9_Puas
total_Puas = prob_count_A9_sb_Puas + \
    prob_count_A9_b_Puas + prob_count_A9_c_Puas+prob_count_A9_k_Puas+prob_count_A9_sk_Puas

# Menyusun data untuk tabel kolom A9
data_table = [
    ["sb", count_A9_sb_Tpuas, count_A9_sb_Puas, round(
        prob_count_A9_sb_Tpuas, 2), round(prob_count_A9_sb_Puas, 2)],
    ["b", count_A9_b_Tpuas, count_A9_b_Puas, round(
        prob_count_A9_b_Tpuas, 2), round(prob_count_A9_b_Puas, 2)],
    ["c", count_A9_c_Tpuas, count_A9_c_Puas, round(
        prob_count_A9_c_Tpuas, 2), round(prob_count_A9_c_Puas, 2)],
    ["k", count_A9_k_Tpuas, count_A9_k_Puas, round(
        prob_count_A9_k_Tpuas, 2), round(prob_count_A9_k_Puas, 2)],
    ["sk", count_A9_sk_Tpuas, count_A9_sk_Puas, round(
        prob_count_A9_sk_Tpuas, 2), round(prob_count_A9_sk_Puas, 2)],
    ["Total", total_A9_Tpuas, total_A9_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A9
table_headers = ["A9", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A10
prob_A10 = df['A10'].head(81).value_counts()
print(prob_A10)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A10 = data_naivebayes["A10"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A10
count_A10_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A10']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A10_b_Tpuas = data_naivebayes.loc[data_naivebayes['A10']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A10_c_Tpuas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A10_k_Tpuas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A10_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A10_Tpuas = count_A10_sb_Tpuas + \
    count_A10_b_Tpuas+count_A10_c_Tpuas + count_A10_k_Tpuas + count_A10_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A10
count_A10_sb_Puas = data_naivebayes.loc[data_naivebayes['A10']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A10_b_Puas = data_naivebayes.loc[data_naivebayes['A10']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A10_c_Puas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A10_k_Puas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A10_sk_Puas = data_naivebayes.loc[data_naivebayes['A10']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A10_Puas = count_A10_sb_Puas + \
    count_A10_b_Puas+count_A10_c_Puas+count_A10_k_Puas+count_A10_sk_Puas

# probabilitas Tpuas kolom A10
prob_count_A10_sb_Tpuas = count_A10_sb_Tpuas / \
    total_A10_Tpuas
prob_count_A10_b_Tpuas = count_A10_b_Tpuas / \
    total_A10_Tpuas
prob_count_A10_c_Tpuas = count_A10_c_Tpuas / \
    total_A10_Tpuas
prob_count_A10_k_Tpuas = count_A10_k_Tpuas / \
    total_A10_Tpuas
prob_count_A10_sk_Tpuas = count_A10_sk_Tpuas / \
    total_A10_Tpuas  
total_Tpuas = prob_count_A10_sb_Tpuas + \
    prob_count_A10_b_Tpuas + prob_count_A10_c_Tpuas+prob_count_A10_k_Tpuas+prob_count_A10_sk_Tpuas

# probabilitas Puas kolom A10
prob_count_A10_sb_Puas = count_A10_sb_Puas / \
    total_A10_Puas
prob_count_A10_b_Puas = count_A10_b_Puas / \
    total_A10_Puas
prob_count_A10_c_Puas = count_A10_c_Puas / \
    total_A10_Puas
prob_count_A10_k_Puas = count_A10_k_Puas / \
    total_A10_Puas
prob_count_A10_sk_Puas = count_A10_sk_Puas / \
    total_A10_Puas
total_Puas = prob_count_A10_sb_Puas + \
    prob_count_A10_b_Puas + prob_count_A10_c_Puas+prob_count_A10_k_Puas+prob_count_A10_sk_Puas

# Menyusun data untuk tabel kolom A10
data_table = [
    ["sb", count_A10_sb_Tpuas, count_A10_sb_Puas, round(
        prob_count_A10_sb_Tpuas, 2), round(prob_count_A10_sb_Puas, 2)],
    ["b", count_A10_b_Tpuas, count_A10_b_Puas, round(
        prob_count_A10_b_Tpuas, 2), round(prob_count_A10_b_Puas, 2)],
    ["c", count_A10_c_Tpuas, count_A10_c_Puas, round(
        prob_count_A10_c_Tpuas, 2), round(prob_count_A10_c_Puas, 2)],
    ["k", count_A10_k_Tpuas, count_A10_k_Puas, round(
        prob_count_A10_k_Tpuas, 2), round(prob_count_A10_k_Puas, 2)],
    ["sk", count_A10_sk_Tpuas, count_A10_sk_Puas, round(
        prob_count_A10_sk_Tpuas, 2), round(prob_count_A10_sk_Puas, 2)],
    ["Total", total_A10_Tpuas, total_A10_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A10
table_headers = ["A10", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM A11
prob_A11 = df['A11'].head(81).value_counts()
print(prob_A11)

data_naivebayes = df.head(80)
Hasil = data_naivebayes["Hasil"]
A11 = data_naivebayes["A11"]

# Jumlah Kejadian berdasarkan Hasil Tpuas kolom A11
count_A11_sb_Tpuas = data_naivebayes.loc[data_naivebayes['A11']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A11_b_Tpuas = data_naivebayes.loc[data_naivebayes['A11']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A11_c_Tpuas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A11_k_Tpuas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
count_A11_sk_Tpuas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Tpuas'].shape[0]
total_A11_Tpuas = count_A11_sb_Tpuas + \
    count_A11_b_Tpuas+count_A11_c_Tpuas + count_A11_k_Tpuas + count_A11_sk_Tpuas  

# Jumlah Kejadian berdasarkan Hasil Puas kolom A11
count_A11_sb_Puas = data_naivebayes.loc[data_naivebayes['A11']
                                             == 'sb'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A11_b_Puas = data_naivebayes.loc[data_naivebayes['A11']
                                               == 'b'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A11_c_Puas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'c'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A11_k_Puas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'k'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
count_A11_sk_Puas = data_naivebayes.loc[data_naivebayes['A11']
                                            == 'sk'].loc[data_naivebayes['Hasil'] == 'Puas'].shape[0]
total_A11_Puas = count_A11_sb_Puas + \
    count_A11_b_Puas+count_A11_c_Puas+count_A11_k_Puas+count_A11_sk_Puas

# probabilitas Tpuas kolom A11
prob_count_A11_sb_Tpuas = count_A11_sb_Tpuas / \
    total_A11_Tpuas
prob_count_A11_b_Tpuas = count_A11_b_Tpuas / \
    total_A11_Tpuas
prob_count_A11_c_Tpuas = count_A11_c_Tpuas / \
    total_A11_Tpuas
prob_count_A11_k_Tpuas = count_A11_k_Tpuas / \
    total_A11_Tpuas
prob_count_A11_sk_Tpuas = count_A11_sk_Tpuas / \
    total_A11_Tpuas  
total_Tpuas = prob_count_A11_sb_Tpuas + \
    prob_count_A11_b_Tpuas + prob_count_A11_c_Tpuas+prob_count_A11_k_Tpuas+prob_count_A11_sk_Tpuas

# probabilitas Puas kolom A11
prob_count_A11_sb_Puas = count_A11_sb_Puas / \
    total_A11_Puas
prob_count_A11_b_Puas = count_A11_b_Puas / \
    total_A11_Puas
prob_count_A11_c_Puas = count_A11_c_Puas / \
    total_A11_Puas
prob_count_A11_k_Puas = count_A11_k_Puas / \
    total_A11_Puas
prob_count_A11_sk_Puas = count_A11_sk_Puas / \
    total_A11_Puas
total_Puas = prob_count_A11_sb_Puas + \
    prob_count_A11_b_Puas + prob_count_A11_c_Puas+prob_count_A11_k_Puas+prob_count_A11_sk_Puas

# Menyusun data untuk tabel kolom A11
data_table = [
    ["sb", count_A11_sb_Tpuas, count_A11_sb_Puas, round(
        prob_count_A11_sb_Tpuas, 2), round(prob_count_A11_sb_Puas, 2)],
    ["b", count_A11_b_Tpuas, count_A11_b_Puas, round(
        prob_count_A11_b_Tpuas, 2), round(prob_count_A11_b_Puas, 2)],
    ["c", count_A11_c_Tpuas, count_A11_c_Puas, round(
        prob_count_A11_c_Tpuas, 2), round(prob_count_A11_c_Puas, 2)],
    ["k", count_A11_k_Tpuas, count_A11_k_Puas, round(
        prob_count_A11_k_Tpuas, 2), round(prob_count_A11_k_Puas, 2)],
    ["sk", count_A11_sk_Tpuas, count_A11_sk_Puas, round(
        prob_count_A11_sk_Tpuas, 2), round(prob_count_A11_sk_Puas, 2)],
    ["Total", total_A11_Tpuas, total_A11_Puas,
        round(total_Tpuas, 2), round(total_Puas, 2)]
]

# Menampilkan tabel kolom A11
table_headers = ["A11", "Tpuas", "Puas",
                 "Probabilitas Tpuas", "Probabilitas Puas"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

print("======================================")
# Meminta inputan user
A1 = input("Masukkan nilai A1 (sb/b/c/k/sk): ")
A2 = input("Masukkan nilai A2 (sb/b/c/k/sk): ")
A3 = input("Masukkan nilai A3 (sb/b/c/k/sk): ")
A4 = input("Masukkan nilai A4 (sb/b/c/k/sk): ")
A5 = input("Masukkan nilai A5 (sb/b/c/k/sk): ")
A6 = input("Masukkan nilai A6 (sb/b/c/k/sk): ")
A7 = input("Masukkan nilai A7 (sb/b/c/k/sk): ")
A8 = input("Masukkan nilai A8 (sb/b/c/k/sk): ")
A9 = input("Masukkan nilai A9 (sb/b/c/k/sk): ")
A10 = input("Masukkan nilai A10 (sb/b/c/k/sk): ")
A11 = input("Masukkan nilai A11 (sb/b/c/k/sk): ")

# Cek inputan 
if A1 == "sb":
    A1_Tpuas = prob_count_A1_sb_Tpuas
    A1_Puas = prob_count_A1_sb_Puas
elif A1 == "b":
    A1_Tpuas = prob_count_A1_b_Tpuas
    A1_Puas = prob_count_A1_b_Puas
elif A1 == "c":
    A1_Tpuas = prob_count_A1_c_Tpuas
    A1_Puas = prob_count_A1_c_Puas
elif A1 == "k":
    A1_Tpuas = prob_count_A1_k_Tpuas
    A1_Puas = prob_count_A1_k_Puas
else:
    A1_Tpuas = prob_count_A1_sk_Tpuas
    A1_Puas = prob_count_A1_sk_Puas


if A2 == "sb":
    A2_Tpuas = prob_count_A2_sb_Tpuas
    A2_Puas = prob_count_A2_sb_Puas
elif A2 == "b":
    A2_Tpuas = prob_count_A2_b_Tpuas
    A2_Puas = prob_count_A2_b_Puas
elif A2 == "c":
    A2_Tpuas = prob_count_A2_c_Tpuas
    A2_Puas = prob_count_A2_c_Puas
elif A2 == "k":
    A2_Tpuas = prob_count_A2_k_Tpuas
    A2_Puas = prob_count_A2_k_Puas
else:
    A2_Tpuas = prob_count_A2_sk_Tpuas
    A2_Puas = prob_count_A2_sk_Puas
    
    
if A3 == "sb":
    A3_Tpuas = prob_count_A3_sb_Tpuas
    A3_Puas = prob_count_A3_sb_Puas
elif A3 == "b":
    A3_Tpuas = prob_count_A3_b_Tpuas
    A3_Puas = prob_count_A3_b_Puas
elif A3 == "c":
    A3_Tpuas = prob_count_A3_c_Tpuas
    A3_Puas = prob_count_A3_c_Puas
elif A3 == "k":
    A3_Tpuas = prob_count_A3_k_Tpuas
    A3_Puas = prob_count_A3_k_Puas
else:
    A3_Tpuas = prob_count_A3_sk_Tpuas
    A3_Puas = prob_count_A3_sk_Puas
    
    
if A4 == "sb":
    A4_Tpuas = prob_count_A4_sb_Tpuas
    A4_Puas = prob_count_A4_sb_Puas
elif A4 == "b":
    A4_Tpuas = prob_count_A4_b_Tpuas
    A4_Puas = prob_count_A4_b_Puas
elif A4 == "c":
    A4_Tpuas = prob_count_A4_c_Tpuas
    A4_Puas = prob_count_A4_c_Puas
elif A4 == "k":
    A4_Tpuas = prob_count_A4_k_Tpuas
    A4_Puas = prob_count_A4_k_Puas
else:
    A4_Tpuas = prob_count_A4_sk_Tpuas
    A4_Puas = prob_count_A4_sk_Puas
    
    
if A5 == "sb":
    A5_Tpuas = prob_count_A5_sb_Tpuas
    A5_Puas = prob_count_A5_sb_Puas
elif A5 == "b":
    A5_Tpuas = prob_count_A5_b_Tpuas
    A5_Puas = prob_count_A5_b_Puas
elif A5 == "c":
    A5_Tpuas = prob_count_A5_c_Tpuas
    A5_Puas = prob_count_A5_c_Puas
elif A5 == "k":
    A5_Tpuas = prob_count_A5_k_Tpuas
    A5_Puas = prob_count_A5_k_Puas
else:
    A5_Tpuas = prob_count_A5_sk_Tpuas
    A5_Puas = prob_count_A5_sk_Puas
    
    
if A6 == "sb":
    A6_Tpuas = prob_count_A6_sb_Tpuas
    A6_Puas = prob_count_A6_sb_Puas
elif A6 == "b":
    A6_Tpuas = prob_count_A6_b_Tpuas
    A6_Puas = prob_count_A6_b_Puas
elif A6 == "c":
    A6_Tpuas = prob_count_A6_c_Tpuas
    A6_Puas = prob_count_A6_c_Puas
elif A6 == "k":
    A6_Tpuas = prob_count_A6_k_Tpuas
    A6_Puas = prob_count_A6_k_Puas
else:
    A6_Tpuas = prob_count_A6_sk_Tpuas
    A6_Puas = prob_count_A6_sk_Puas
    
    
if A7 == "sb":
    A7_Tpuas = prob_count_A7_sb_Tpuas
    A7_Puas = prob_count_A7_sb_Puas
elif A7 == "b":
    A7_Tpuas = prob_count_A7_b_Tpuas
    A7_Puas = prob_count_A7_b_Puas
elif A7 == "c":
    A7_Tpuas = prob_count_A7_c_Tpuas
    A7_Puas = prob_count_A7_c_Puas
elif A7 == "k":
    A7_Tpuas = prob_count_A7_k_Tpuas
    A7_Puas = prob_count_A7_k_Puas
else:
    A7_Tpuas = prob_count_A7_sk_Tpuas
    A7_Puas = prob_count_A7_sk_Puas
    
    
if A8 == "sb":
    A8_Tpuas = prob_count_A8_sb_Tpuas
    A8_Puas = prob_count_A8_sb_Puas
elif A8 == "b":
    A8_Tpuas = prob_count_A8_b_Tpuas
    A8_Puas = prob_count_A8_b_Puas
elif A8 == "c":
    A8_Tpuas = prob_count_A8_c_Tpuas
    A8_Puas = prob_count_A8_c_Puas
elif A8 == "k":
    A8_Tpuas = prob_count_A8_k_Tpuas
    A8_Puas = prob_count_A8_k_Puas
else:
    A8_Tpuas = prob_count_A8_sk_Tpuas
    A8_Puas = prob_count_A8_sk_Puas
    
    
if A9 == "sb":
    A9_Tpuas = prob_count_A9_sb_Tpuas
    A9_Puas = prob_count_A9_sb_Puas
elif A9 == "b":
    A9_Tpuas = prob_count_A9_b_Tpuas
    A9_Puas = prob_count_A9_b_Puas
elif A9 == "c":
    A9_Tpuas = prob_count_A9_c_Tpuas
    A9_Puas = prob_count_A9_c_Puas
elif A9 == "k":
    A9_Tpuas = prob_count_A9_k_Tpuas
    A9_Puas = prob_count_A9_k_Puas
else:
    A9_Tpuas = prob_count_A9_sk_Tpuas
    A9_Puas = prob_count_A9_sk_Puas
    
    
if A10 == "sb":
    A10_Tpuas = prob_count_A10_sb_Tpuas
    A10_Puas = prob_count_A10_sb_Puas
elif A10 == "b":
    A10_Tpuas = prob_count_A10_b_Tpuas
    A10_Puas = prob_count_A10_b_Puas
elif A10 == "c":
    A10_Tpuas = prob_count_A10_c_Tpuas
    A10_Puas = prob_count_A10_c_Puas
elif A10 == "k":
    A10_Tpuas = prob_count_A10_k_Tpuas
    A10_Puas = prob_count_A10_k_Puas
else:
    A10_Tpuas = prob_count_A10_sk_Tpuas
    A10_Puas = prob_count_A10_sk_Puas
    
    
if A11 == "sb":
    A11_Tpuas = prob_count_A11_sb_Tpuas
    A11_Puas = prob_count_A11_sb_Puas
elif A11 == "b":
    A11_Tpuas = prob_count_A11_b_Tpuas
    A11_Puas = prob_count_A11_b_Puas
elif A11 == "c":
    A11_Tpuas = prob_count_A11_c_Tpuas
    A11_Puas = prob_count_A11_c_Puas
elif A11 == "k":
    A11_Tpuas = prob_count_A11_k_Tpuas
    A11_Puas = prob_count_A11_k_Puas
else:
    A11_Tpuas = prob_count_A11_sk_Tpuas
    A11_Puas = prob_count_A11_sk_Puas

Tpuas = A1_Tpuas * A2_Tpuas * A3_Tpuas * A4_Tpuas * A5_Tpuas * A6_Tpuas * A7_Tpuas * A8_Tpuas * A9_Tpuas * A10_Tpuas * A11_Tpuas * jumlah_Tpuas
Puas = A1_Puas * A2_Puas * A3_Puas * A4_Puas * A5_Puas * A6_Puas * A7_Puas * A8_Puas * A9_Puas * A10_Puas * A11_Puas * jumlah_Puas

if Puas > Tpuas:
    Hasil = "Puas"
else:
    Hasil = "Tidak Puas"

hasil_desimal_Puas = '{:.15f}'.format(Puas)
hasil_desimal_TPuas = '{:.15f}'.format(Tpuas)

print("======================================")
print(f"Probabilitas Puas: {hasil_desimal_Puas}")
print(f"Probabilitas Tidak puas: {hasil_desimal_TPuas}")
print(f"Hasil Prediksi: {Hasil}")