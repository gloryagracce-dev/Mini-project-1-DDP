# Program Kelola Daftar Buku Sedang Dibaca
daftar_buku = [] # Tempat simpaan data pakai list
while True: # Perulangan menu
    print("\n=====MENU DAFTAR BUKU=====")
    print("1. Tambah Buku")
    print("2. Lihat Semua Buku")
    print("3. Ubah Data Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan angka [1-5]: ")
    # Validasi pilihan
    if pilihan not in ["1", "2", "3", "4", "5",]:
        print("Pilihan tidak ada! Coba lagi.")
        continue
    # === PILIHAN 1: TAMBAH BUKU ===
    if pilihan == "1":
        nama = input("Masukkan nama buku: ")
        hal = input("Masukkan halaman terakhir dibaca: ")
        daftar_buku.append( (nama, hal) ) # simpan pakai  tuple
        print("Berhasil ditambahkan!")
        # === PILIHAN 2: LIHAT SEMUA ===
    elif pilihan == "2":
        if len(daftar_buku) == 0:
            print("Belum ada catatan buku.")
        else:
            print("\n--- DAFTAR BUKU ---")
            for i, buku in enumerate(daftar_buku, start=1):
                print(f"{i}. Judul: {buku[0]} | Halaman: {buku[1]}")
    # === PILIHAN 3: UBAH DATA ===
    elif pilihan == "3":
        if len(daftar_buku) == 0:
            print("Belum ada data buku.")
        else:
            nomor = int(input("Masukkan nomor buku yang mau diubah: ")) - 1
            if 0 <= nomor < len(daftar_buku):
                nama_baru = input("Masukkan judul baru: ")
                hal_baru = input("Masukkan halaman baru: ")
                daftar_buku[nomor] = (nama_baru, hal_baru)
                print("Berhasil diubah!")
            else:
                print("Nomor buku tidak ada!")
    # === PILIHAN 4: HAPUS BUKU ===
    elif pilihan == "4":
        if len(daftar_buku) == 0:
            print("Belum ada data buku.")
        else:
            nomor = int(input("Masukkan nomor buku yang mau dihapus: ")) - 1
            if 0 <= nomor < len(daftar_buku):
                daftar_buku.pop(nomor)
                print("Berhasil dihapus!")
            else:
                print("Nomor buku tidak ada!")
    # === PILIHAN 5: KELUAR ===
    elif pilihan == "5":
        print("Program selesai, Terima Kasih!")
        break


