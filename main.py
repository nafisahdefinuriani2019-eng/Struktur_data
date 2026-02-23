buku = {
    "Python Dasar": 3,
    "Algoritma": 2,
    "Struktur Data": 1
}

while True:
    print("\n=== SISTEM PERPUSTAKAAN ===")
    print("1. Lihat Daftar Buku")
    print("2. Tambah Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan Buku")
    print("5. Cari Buku")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        print("\nDaftar Buku:")
        for judul, stok in buku.items():
            print(f"{judul} - Stok: {stok}")

    elif pilihan == "2":
        judul = input("Masukkan judul buku: ")
        stok = int(input("Masukkan jumlah stok: "))
        buku[judul] = stok
        print("Buku berhasil ditambahkan.")

    elif pilihan == "3":
        judul = input("Masukkan judul buku yang ingin dipinjam: ")
        if judul in buku and buku[judul] > 0:
            buku[judul] -= 1
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak tersedia atau tidak ditemukan.")

    elif pilihan == "4":
        judul = input("Masukkan judul buku yang dikembalikan: ")
        if judul in buku:
            buku[judul] += 1
            print("Buku berhasil dikembalikan.")
        else:
            print("Judul tidak ditemukan.")

    elif pilihan == "5":
        judul = input("Masukkan judul buku yang dicari: ")
        if judul in buku:
            print(f"Buku tersedia dengan stok: {buku[judul]}")
        else:
            print("Buku tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
