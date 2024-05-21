data_barang = [
    "kecap",
    "telur",
    "terigu",
    "gula",
]

def tambah_data(nama):
    data_barang.append(nama)
    print(f"Barang bernama {nama} ditambahkan ke daftar.")

def print_barang():
    print("Daftar barang saat ini:")
    for i, nama in enumerate(data_barang):
        print(f"{i+1}: {nama}")

def hapus_barang(nama):
  #Fungsi untuk menghapus barang dari daftar berdasarkan nama.
#Args:
      #nama: Nama barang yang ingin dihapus.
  #Returns:
      #True jika barang berhasil dihapus, False jika tidak ditemukan.

  if nama in data_barang:
    data_barang.remove(nama)
    print(f"Barang bernama {nama} berhasil dihapus dari daftar.")
    return True
  else:
    print(f"Barang bernama {nama} tidak ditemukan dalam daftar.")
    return False

while True:
    print("\nSelamat datang di program Manajemen Stok Barang!")
    print("1. Tambah Data Barang")
    print("2. Hapus Data Barang")
    print("3. Tampilkan Data Barang")
    print("4. Keluar")

    Pilihan = input("Pilihanmu: ")

    if Pilihan == '1':
        nama = input("Masukan Nama barang: ")
        tambah_data(nama)
    elif Pilihan == '2':
        nama_hapus = input("Masukan nama barang yang ingin dihapus: ")
        if hapus_barang(nama_hapus):
          # Barang berhasil dihapus
          pass
        else:
          # Barang tidak ditemukan
          pass
    elif Pilihan == '3':
        print_barang()
    elif Pilihan == '4':
        break
    else:
        print("Pilihan tidak tersedia.")
