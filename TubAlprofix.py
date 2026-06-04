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

    print("No  Nama                 Pinjaman (Rp)    Tenor   Bunga      Status")
    print("-------------------------------------------------------------------")  

    for i in range(len(nama_peminjam)):
        print(str(i + 1) + ".  " + nama_peminjam[i] + "   Rp" + str(jumlah_pinjaman[i]) + "   " + str(tenor_pinjaman[i]) + " bln   " + jenis_bunga[i] + "   " + status_pinjaman[i])

    print("-------------------------------------------------------------------")
    print("Total peminjam: " + str(len(nama_peminjam)) + " orang")

def menu_utama():
    while True:
        print("\n========================================")   
        print("   SIMULASI PINJAMAN DAN KREDIT BANK")
        print("========================================")
        print("1. Tambah Data Peminjam")
        print("2. Lihat Daftar Peminjam")
        print("0. Keluar")
        print("========================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_peminjam()
        elif pilihan == "2":
            tampilkan_semua()
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak tersedia, coba lagi.")


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

    # menentukan bunga
    if bunga == "tetap":
        persen_bunga = 0.05
    else:
        persen_bunga = 0.08

    # perhitungan
    total_bunga = pinjaman * persen_bunga
    total_bayar = pinjaman + total_bunga
    cicilan_per_bulan = total_bayar / tenor

    print("\n--- DETAIL CICILAN ---")
    print("Nama Peminjam      :", nama_peminjam[nomor])
    print("Jumlah Pinjaman    : Rp", pinjaman)
    print("Total Bunga        : Rp", total_bunga)
    print("Total Pembayaran   : Rp", total_bayar)
    print("Cicilan Per Bulan  : Rp", round(cicilan_per_bulan, 2))
menu_utama()
hitung_cicilan()