data_barang = ["Laptop Lenovo A1","Laptop Lenovo A2","Laptop Lenovo A3","Laptop Lenovo A4"]
stok_barang = {
    "Laptop Lenovo A1": 0,
    "Laptop Lenovo A2": 0,
    "Laptop Lenovo A3": 0,
    "Laptop Lenovo A4": 0,
}

def tambah_data(nama, stok):
  data_barang.append(nama)
  stok_barang[nama] = stok
  print(f"Barang bernama {nama} dengan stok {stok} ditambahkan ke daftar.")

def print_barang():
  print("Daftar barang saat ini:")
  for i, nama in enumerate(data_barang):
    print(f"{i+1}: {nama} - Stok: {stok_barang[nama]}")

def hapus_barang(nama):
  if nama in data_barang:
    stok_barang[nama] -= 1
    data_barang.remove(nama)
    print(f"Barang bernama {nama} berhasil dihapus dari daftar. Stok tersisa: {stok_barang[nama]}")
  else:
    print(f"Barang bernama {nama} tidak ditemukan dalam daftar.")

def edit_data(nama):
  if nama in data_barang:
    # Tampilkan data barang yang akan diedit
    print(f"Data Barang {nama}:")
    print(f"- Stok: {stok_barang[nama]}")

    # Minta input baru untuk nama dan stok
    nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin diubah): ")
    stok_baru = int(input("Masukkan stok baru: "))

    # Perbarui data barang
    if nama_baru:
      data_barang[data_barang.index(nama)] = nama_baru
    stok_barang[nama] = stok_baru
    print(f"Data barang {nama} diubah menjadi:")
    print(f"- Nama: {nama_baru if nama_baru else nama}")
    print(f"- Stok: {stok_baru}")
  else:
    print(f"Barang bernama {nama} tidak ditemukan dalam daftar.")

while True:
  print("\nSelamat datang di program Manajemen Stok Barang!")
  print("1. Tambah Data Barang")
  print("2. Tampilkan Stok Barang")
  print("3. Edit Data Barang")
  print("4. Hapus Data Barang")
  print("5. Keluar")

  Pilihan = input("Pilihanmu: ")

  if Pilihan == '1':
    nama = input("Masukan Nama barang: ")
    stok = int(input("Masukan jumlah stok: "))
    tambah_data(nama, stok)
  elif Pilihan == '2':
    print_barang()
  elif Pilihan == '3':
    nama_edit = input("Masukkan nama barang yang ingin diedit: ")
    edit_data(nama_edit)
  elif Pilihan == '4':
    nama_hapus = input("Masukan nama barang yang ingin dihapus: ")
    hapus_barang(nama_hapus)
  elif Pilihan == '5':
    break
  else:
    print("Pilihan tidak tersedia.")
