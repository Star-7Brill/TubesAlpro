# Aplikasi Simulasi Pinjaman dan Kredit Uang Sederhana

nama_peminjam   = []
jumlah_pinjaman = []
tenor_pinjaman  = []
jenis_bunga     = []
status_pinjaman = []

def tambah_peminjam():
    print("\n--- TAMBAH DATA PEMINJAM ---")      

    nama     = input("Nama peminjam        : ")
    pinjaman = float(input("Jumlah pinjaman (Rp) : "))
    tenor    = int(input("Tenor (bulan)        : "))
    bunga    = input("Jenis bunga (tetap/variabel): ")

    nama_peminjam.append(nama)
    jumlah_pinjaman.append(pinjaman)
    tenor_pinjaman.append(tenor)
    jenis_bunga.append(bunga)
    status_pinjaman.append("cicilan")

    print("Data " + nama + " berhasil ditambahkan!")

def tampilkan_semua():
    print("\n--- DAFTAR PEMINJAM ---")

    if len(nama_peminjam) == 0:
        print("Belum ada data peminjam.")
        return

    print("No  Nama                 Pinjaman (Rp)    Tenor   Bunga     Status")
    print("-------------------------------------------------------------------")  

    for i in range(len(nama_peminjam)):
        print(str(i + 1) + ".  " + nama_peminjam[i] + "   Rp" + str(jumlah_pinjaman[i]) + "   " + str(tenor_pinjaman[i]) + " bln   " + jenis_bunga[i] + "   " + status_pinjaman[i])

    print("-------------------------------------------------------------------")
    print("Total peminjam: " + str(len(nama_peminjam)) + " orang")

def hapus_peminjam():
    print("\n--- HAPUS DATA PEMINJAM ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data!")
        return
    tampilkan_semua()
    nomor = int(input("Pilih nomor peminjam yang ingin dihapus: ")) - 1

    if nomor < 0 or nomor >= len(nama_peminjam):
        print("Nomor tidak valid!")
        return
    
    nama_dihapus = nama_peminjam[nomor]

    nama_peminjam.pop(nomor)
    jumlah_pinjaman.pop(nomor)
    tenor_pinjaman.pop(nomor)
    jenis_bunga.pop(nomor)
    status_pinjaman.pop(nomor)

    print("Data " + nama_dihapus + " berhasil dihapus!")


def update_peminjam():
    print("\n--- UPDATE DATA PEMINJAM ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data!")
        return
    tampilkan_semua()
    nomor = int(input("Pilih nomor peminjam yang ingin diupdate: ")) - 1

    if nomor < 0 or nomor >= len(nama_peminjam):
        print("Nomor tidak valid!")
        return

    nama_peminjam[nomor] = input("Nama baru: ")
    jumlah_pinjaman[nomor] = float(input("Jumlah pinjaman baru (Rp): "))
    tenor_pinjaman[nomor] = int(input("Tenor baru (bulan): "))
    jenis_bunga[nomor] = input("Jenis bunga baru (tetap/variabel): ")
    print("Data berhasil diupdate!")



def hitung_cicilan():
    print("\n--- HITUNG CICILAN ---")

    if len(nama_peminjam) == 0:
        print("Belum ada data.")
        return

    tampilkan_semua()

    nomor = int(input("Pilih nomor peminjam: ")) - 1

    if nomor < 0 or nomor >= len(nama_peminjam):
        print("Nomor tidak valid.")
        return

    pinjaman = jumlah_pinjaman[nomor]
    tenor = tenor_pinjaman[nomor]
    bunga = jenis_bunga[nomor]

    
    if bunga == "tetap":
        persen_bunga = 0.05
    else:
        persen_bunga = 0.08


    total_bunga = pinjaman * persen_bunga
    total_bayar = pinjaman + total_bunga
    cicilan_per_bulan = total_bayar / tenor

    print("\n--- DETAIL CICILAN ---")
    print("Nama Peminjam      :", nama_peminjam[nomor])
    print("Jumlah Pinjaman    : Rp", pinjaman)
    print("Total Bunga        : Rp", total_bunga)
    print("Total Pembayaran   : Rp", total_bayar)
    print("Cicilan Per Bulan  : Rp", round(cicilan_per_bulan, 2))

def urutkan_selection_sort():
    print("\n--- SELECTION SORT (Berdasarkan Pinjaman Terkecil) ---")
    n = len(nama_peminjam)
    if n == 0:
        print("Belum ada data untuk diurutkan.")
        return

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if jumlah_pinjaman[j] < jumlah_pinjaman[min_idx]:
                min_idx = j
        
        
        jumlah_pinjaman[i], jumlah_pinjaman[min_idx] = jumlah_pinjaman[min_idx], jumlah_pinjaman[i]
        nama_peminjam[i], nama_peminjam[min_idx]     = nama_peminjam[min_idx], nama_peminjam[i]
        tenor_pinjaman[i], tenor_pinjaman[min_idx]   = tenor_pinjaman[min_idx], tenor_pinjaman[i]
        jenis_bunga[i], jenis_bunga[min_idx]         = jenis_bunga[min_idx], jenis_bunga[i]
        status_pinjaman[i], status_pinjaman[min_idx] = status_pinjaman[min_idx], status_pinjaman[i]

    print("Data berhasil diurutkan dengan Selection Sort!")
    tampilkan_semua()

def urutkan_insertion_sort():
    print("\n--- INSERTION SORT (Berdasarkan Pinjaman Terkecil) ---")
    n = len(nama_peminjam)
    if n == 0:
        print("Belum ada data untuk diurutkan.")
        return

    for i in range(1, n):
        key_pinjaman = jumlah_pinjaman[i]
        key_nama     = nama_peminjam[i]
        key_tenor    = tenor_pinjaman[i]
        key_bunga    = jenis_bunga[i]
        key_status   = status_pinjaman[i]
        
        j = i - 1
        while j >= 0 and key_pinjaman < jumlah_pinjaman[j]:
            jumlah_pinjaman[j + 1] = jumlah_pinjaman[j]
            nama_peminjam[j + 1]   = nama_peminjam[j]
            tenor_pinjaman[j + 1]  = tenor_pinjaman[j]
            jenis_bunga[j + 1]     = jenis_bunga[j]
            status_pinjaman[j + 1] = status_pinjaman[j]
            j -= 1
            
        jumlah_pinjaman[j + 1] = key_pinjaman
        nama_peminjam[j + 1]   = key_nama
        tenor_pinjaman[j + 1]  = key_tenor
        jenis_bunga[j + 1]     = key_bunga
        status_pinjaman[j + 1] = key_status

    print("Data berhasil diurutkan dengan Insertion Sort!")
    tampilkan_semua()


def menu_utama_baru():
    while True:
        print("\n========================================")   
        print("   SIMULASI PINJAMAN DAN KREDIT BANK")
        print("========================================")
        print("1. Tambah Data Peminjam")
        print("2. Lihat Daftar Peminjam")
        print("3. Update Data Peminjam")
        print("4. Hapus Data Peminjam")
        print("5. Hitung Cicilan")
        print("6. Urutkan Data (Selection Sort)")
        print("7. Urutkan Data (Insertion Sort)")
        print("0. Keluar")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_peminjam()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "3":
            update_peminjam()
        elif pilihan == "4":
            hapus_peminjam()
        elif pilihan == "5":
            hitung_cicilan()
        elif pilihan == "6":
            urutkan_selection_sort()
        elif pilihan == "7":
            urutkan_insertion_sort()
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak tersedia, coba lagi.")

# Menjalankan menu baru yang sudah terintegrasi fitur sorting
menu_utama_baru()