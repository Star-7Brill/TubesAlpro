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
    status   = input("Status peminjaman (cicilan/lunas): ")

    nama_peminjam.append(nama)
    jumlah_pinjaman.append(pinjaman)
    tenor_pinjaman.append(tenor)
    jenis_bunga.append(bunga)
    status_pinjaman.append(status)

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
    status_pinjaman[nomor] = input("Status peminjaman(cicilan/lunas): ")
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
    print("\n--- SELECTION SORT ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data untuk diurutkan.")
        return

    print("Urutkan berdasarkan:")
    print("1. Nama Peminjam")
    print("2. Jumlah Pinjaman")
    print("3. Tenor")
    print("4. Jenis Bunga")
    print("5. Status")
    kriteria = input("Pilih kriteria: ")

    print("Arah urutan:")
    print("1. Ascending (A-Z / terkecil ke terbesar)")
    print("2. Descending (Z-A / terbesar ke terkecil)")
    arah = input("Pilih arah: ")

    n = len(nama_peminjam)

    for i in range(n):
        idx_terpilih = i

        for j in range(i + 1, n):
            if kriteria == "1":
                nilai_j        = nama_peminjam[j].lower()
                nilai_terpilih = nama_peminjam[idx_terpilih].lower()
            elif kriteria == "2":
                nilai_j        = jumlah_pinjaman[j]
                nilai_terpilih = jumlah_pinjaman[idx_terpilih]
            elif kriteria == "3":
                nilai_j        = tenor_pinjaman[j]
                nilai_terpilih = tenor_pinjaman[idx_terpilih]
            elif kriteria == "4":
                nilai_j        = jenis_bunga[j].lower()
                nilai_terpilih = jenis_bunga[idx_terpilih].lower()
            elif kriteria == "5":
                nilai_j        = status_pinjaman[j].lower()
                nilai_terpilih = status_pinjaman[idx_terpilih].lower()
            else:
                print("Kriteria tidak valid.")
                return

            if arah == "1":
                if nilai_j < nilai_terpilih:
                    idx_terpilih = j
            else:
                if nilai_j > nilai_terpilih:
                    idx_terpilih = j

        nama_peminjam[i],    nama_peminjam[idx_terpilih]   = nama_peminjam[idx_terpilih],   nama_peminjam[i]
        jumlah_pinjaman[i],  jumlah_pinjaman[idx_terpilih] = jumlah_pinjaman[idx_terpilih], jumlah_pinjaman[i]
        tenor_pinjaman[i],   tenor_pinjaman[idx_terpilih]  = tenor_pinjaman[idx_terpilih],  tenor_pinjaman[i]
        jenis_bunga[i],      jenis_bunga[idx_terpilih]     = jenis_bunga[idx_terpilih],     jenis_bunga[i]
        status_pinjaman[i],  status_pinjaman[idx_terpilih] = status_pinjaman[idx_terpilih], status_pinjaman[i]

    print("Data berhasil diurutkan!")
    tampilkan_semua()


def urutkan_insertion_sort():
    print("\n--- INSERTION SORT ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data untuk diurutkan.")
        return

    print("Urutkan berdasarkan:")
    print("1. Nama Peminjam")
    print("2. Jumlah Pinjaman")
    print("3. Tenor")
    print("4. Jenis Bunga")
    print("5. Status")
    kriteria = input("Pilih kriteria: ")

    print("Arah urutan:")
    print("1. Ascending (A-Z / terkecil ke terbesar)")
    print("2. Descending (Z-A / terbesar ke terkecil)")
    arah = input("Pilih arah: ")

    n = len(nama_peminjam)

    for i in range(1, n):
        kunci_nama     = nama_peminjam[i]
        kunci_pinjaman = jumlah_pinjaman[i]
        kunci_tenor    = tenor_pinjaman[i]
        kunci_bunga    = jenis_bunga[i]
        kunci_status   = status_pinjaman[i]

        if kriteria == "1":
            kunci_nilai = kunci_nama.lower()
        elif kriteria == "2":
            kunci_nilai = kunci_pinjaman
        elif kriteria == "3":
            kunci_nilai = kunci_tenor
        elif kriteria == "4":
            kunci_nilai = kunci_bunga.lower()
        elif kriteria == "5":
            kunci_nilai = kunci_status.lower()
        else:
            print("Kriteria tidak valid.")
            return

        j = i - 1

        while j >= 0:
            if kriteria == "1":
                nilai_j = nama_peminjam[j].lower()
            elif kriteria == "2":
                nilai_j = jumlah_pinjaman[j]
            elif kriteria == "3":
                nilai_j = tenor_pinjaman[j]
            elif kriteria == "4":
                nilai_j = jenis_bunga[j].lower()
            elif kriteria == "5":
                nilai_j = status_pinjaman[j].lower()

            if arah == "1":
                harus_geser = nilai_j > kunci_nilai
            else:
                harus_geser = nilai_j < kunci_nilai

            if harus_geser:
                nama_peminjam[j + 1]   = nama_peminjam[j]
                jumlah_pinjaman[j + 1] = jumlah_pinjaman[j]
                tenor_pinjaman[j + 1]  = tenor_pinjaman[j]
                jenis_bunga[j + 1]     = jenis_bunga[j]
                status_pinjaman[j + 1] = status_pinjaman[j]
                j -= 1
            else:
                break

        nama_peminjam[j + 1]   = kunci_nama
        jumlah_pinjaman[j + 1] = kunci_pinjaman
        tenor_pinjaman[j + 1]  = kunci_tenor
        jenis_bunga[j + 1]     = kunci_bunga
        status_pinjaman[j + 1] = kunci_status

    print("Data berhasil diurutkan!")
    tampilkan_semua()

def sequential_search():
    print("\n--- SEQUENTIAL SEARCH ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data.")
        return

    keyword = input("Masukkan nama yang dicari: ").lower()
    hasil   = []

    for i in range(len(nama_peminjam)):
        if keyword in nama_peminjam[i].lower():
            hasil.append(i)

    if len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        print("Data ditemukan:")
        for i in hasil:
            print(str(i + 1) + ". " + nama_peminjam[i] +
                  " - Rp" + str(jumlah_pinjaman[i]) +
                  " - " + str(tenor_pinjaman[i]) + " bln" +
                  " - " + status_pinjaman[i])

def binary_search():
    print("\n--- BINARY SEARCH ---")
    if len(nama_peminjam) == 0:
        print("Belum ada data.")
        return

    # buat salinan indeks terurut berdasarkan nama
    indeks_urut = list(range(len(nama_peminjam)))
    for i in range(1, len(indeks_urut)):
        kunci = indeks_urut[i]
        j = i - 1
        while j >= 0 and nama_peminjam[indeks_urut[j]].lower() > nama_peminjam[kunci].lower():
            indeks_urut[j + 1] = indeks_urut[j]
            j -= 1
        indeks_urut[j + 1] = kunci

    keyword = input("Masukkan nama yang dicari (harus tepat): ").lower()

    kiri   = 0
    kanan  = len(indeks_urut) - 1
    ketemu = False

    while kiri <= kanan:
        tengah   = (kiri + kanan) // 2
        idx      = indeks_urut[tengah]
        nama_cek = nama_peminjam[idx].lower()

        if nama_cek == keyword:
            print("Data ditemukan:")
            print("- Nama    :", nama_peminjam[idx])
            print("- Pinjaman: Rp", jumlah_pinjaman[idx])
            print("- Tenor   :", tenor_pinjaman[idx], "bulan")
            print("- Status  :", status_pinjaman[idx])
            ketemu = True
            break
        elif nama_cek < keyword:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    if not ketemu:
        print("Data tidak ditemukan.")

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
        print("8. Cari Peminjam (Sequential Search)")
        print("9. Cari Peminjam (Binary Search)")
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
        elif pilihan == "8":
            sequential_search()
        elif pilihan == "9":
            binary_search()
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak tersedia, coba lagi.")

# Menjalankan menu baru yang sudah terintegrasi fitur sorting
menu_utama_baru()