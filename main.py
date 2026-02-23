buku = {
    "Python Dasar": 3,
    "Algoritma": 2,
    "Struktur Data": 1
}

dipinjam = []  # List untuk menyimpan buku yang dipinjam

while True:
    print("\n=== SISTEM PERPUSTAKAAN ===")
    print("1. Lihat Daftar Buku")
    print("2. Pinjam Buku")
    print("3. Lihat Buku Dipinjam")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        for judul, stok in buku.items():
            print(f"{judul} - Stok: {stok}")

    elif pilihan == "2":
        judul = input("Masukkan judul buku: ")
        if judul in buku and buku[judul] > 0:
            buku[judul] -= 1
            dipinjam.append(judul)  # masuk ke list
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak tersedia.")

    elif pilihan == "3":
        print("Buku yang sedang dipinjam:")
        for item in dipinjam:
            print(item)

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak valid.")
