from colorama import Fore, Style, init
init(autoreset=True)  # Inisialisasi colorama agar warna reset otomatis setelah print

# Data awal contoh struk pembelanjaan, berisi list dictionary tiap barang
struk = [
    {"id": "A001", "tipe": "Saniteri", "barang": "Sabun Batang", "jumlah": 12, "harga": 10000},
    {"id": "A002", "tipe": "Saniteri", "barang": "Sabun Cair", "jumlah": 2, "harga": 15000},
    {"id": "B001", "tipe": "Minuman", "barang": "Sirup", "jumlah": 1, "harga": 30000},
]

# Kamus tipe barang untuk pilihan input tipe barang berdasarkan nomor
tipe_barang_dict = {
    1: "Saniteri",
    2: "Minuman",
    3: "Makanan",
    4: "Elektronik",
    5: "Pakaian"
}

# Fungsi untuk memformat angka menjadi format ribuan dengan titik (contoh: 10.000)
def format_ribuan(nilai):
    return f"{nilai:,}".replace(",", ".")

# Fungsi untuk menghitung panjang garis pemisah tabel berdasarkan lebar data struk
def hitung_panjang_garis():
    max_id = max((len(item["id"]) for item in struk), default=6)
    max_tipe = max((len(item["tipe"]) for item in struk), default=10)
    max_barang = max((len(item["barang"]) for item in struk), default=14)
    # Total panjang = lebar tiap kolom + margin tetap
    total_panjang = max_id + max_tipe + max_barang + 8 + 8 + 12 + 15
    return total_panjang + 5  # margin tambahan

# Fungsi menampilkan garis horizontal berwarna cyan
def garis(panjang=None):
    if panjang is None:
        panjang = hitung_panjang_garis()
    print(Fore.CYAN + '-' * panjang)

# Fungsi menampilkan header judul dengan garis atas dan bawah
def tampilkan_header_judul(judul):
    panjang = hitung_panjang_garis()
    garis(panjang)
    print(Fore.YELLOW + judul.center(panjang))
    garis(panjang)

# Fungsi menampilkan menu utama dan mengembalikan pilihan pengguna
def tampilkan_menu_utama():
    tampilkan_header_judul('"Struk Pembelanjaan"')
    print('1. Melihat isi Struk Pembelanjaan')
    print('2. Menambah Barang Ke Dalam Struk Pembelanjaan')
    print('3. Mengedit Struk Pembelanjaan')
    print('4. Menghapus Barang Dari Struk Pembelanjaan')
    print('5. Keluar dari Program')
    garis()
    pilihan = input(Fore.GREEN + "Silahkan Pilih angka (1-5): " + Style.RESET_ALL)
    return pilihan

# Fungsi menampilkan menu sub-menu lihat dan mengembalikan pilihan
def tampilkan_menu_lihat():
    tampilkan_header_judul('"Menampilkan Isi Struk Belanja"')
    print('1. Tampilkan Daftar Belanja yang tersedia')
    print('2. Cari ID Barang')
    print('3. Kembali ke Menu Utama')
    garis()
    pilihan = input(Fore.GREEN + "Silahkan Pilih angka (1-3): " + Style.RESET_ALL)
    return pilihan

# Fungsi menampilkan menu sub-menu tambah barang dan mengembalikan pilihan
def tampilkan_menu_tambah():
    tampilkan_header_judul('"Menambahkan Data Struk"')
    print('1. Tambah Barang')
    print('2. Kembali ke Menu Utama')
    garis()
    pilihan = input(Fore.GREEN + "Silahkan Pilih angka (1-2): " + Style.RESET_ALL)
    return pilihan

# Fungsi menampilkan menu sub-menu edit barang dan mengembalikan pilihan
def tampilkan_menu_edit():
    tampilkan_header_judul('"Mengubah Data Struk"')
    print('1. Update Data Barang')
    print('2. Kembali ke Menu Utama')
    garis()
    pilihan = input(Fore.GREEN + "Silahkan Pilih angka (1-2): " + Style.RESET_ALL)
    return pilihan

# Fungsi menampilkan menu sub-menu hapus barang dan mengembalikan pilihan
def tampilkan_menu_hapus():
    tampilkan_header_judul('"Menghapus Data Struk"')
    print('1. Hapus Barang')
    print('2. Kembali ke Menu Utama')
    garis()
    pilihan = input(Fore.GREEN + "Silahkan Pilih angka (1-2): " + Style.RESET_ALL)
    return pilihan

# Fungsi menampilkan data struk dalam bentuk tabel ke terminal
def tampilkan_struk(data):
    panjang = hitung_panjang_garis()
    garis(panjang)
    header = f" {'ID':<6}| {'Tipe':<10}| {'Barang':<14}| {'Jumlah':<8}| {'Harga':<8}| {'Total':<12}"
    print(Fore.YELLOW + header)
    garis(panjang)
    for item in data:
        total = item["jumlah"] * item["harga"]  # Hitung total harga per item
        print(f" {item['id'].upper():<6}| {item['tipe']:<10}| {item['barang']:<14}| "
              f"{item['jumlah']:<8}| {format_ribuan(item['harga']):<8}| {format_ribuan(total):<12}")
    garis(panjang)

# Fungsi mencari barang berdasarkan ID (case insensitive)
def cari_barang_by_id(id_cari):
    hasil = [item for item in struk if item["id"].lower() == id_cari.lower()]
    return hasil

# Fungsi menambah barang baru ke struk dengan validasi input
def tambah_barang():
    while True:
        panjang = hitung_panjang_garis()
        garis(panjang)
        id_baru = input(Fore.GREEN + "Masukkan ID Barang : " + Style.RESET_ALL).strip()
        # Validasi panjang ID
        if len(id_baru) < 4 or len(id_baru) > 6:
            print(Fore.RED + "ID Barang harus antara 4 sampai 6 karakter.")
            continue
        # Cek ID sudah ada atau belum
        if any(item["id"].lower() == id_baru.lower() for item in struk):
            print(Fore.RED + "ID Barang Sudah Tersedia")
            continue
        break

    # Menampilkan pilihan tipe barang dan input tipe baru
    print("Pilih Tipe Barang:")
    for nomor, tipe in tipe_barang_dict.items():
        print(f"{nomor}. {tipe}")

    while True:
        try:
            pilihan_tipe = int(input(Fore.GREEN + "Masukkan nomor tipe barang: " + Style.RESET_ALL))
            if pilihan_tipe not in tipe_barang_dict:
                print(Fore.RED + "Pilihan tipe barang tidak valid.")
                continue
            tipe_baru = tipe_barang_dict[pilihan_tipe]
            break
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid.")

    # Input nama barang dan validasi panjang
    nama_baru = input(Fore.GREEN + "Masukkan Nama Barang : " + Style.RESET_ALL).strip().title()
    if len(nama_baru) < 1 or len(nama_baru) > 50:
        print(Fore.RED + "Nama barang harus antara 1 sampai 50 karakter.")
        return

    # Input jumlah barang dengan validasi angka dan batasan
    while True:
        try:
            jumlah_baru = int(input(Fore.GREEN + "Masukkan Jumlah Barang : " + Style.RESET_ALL))
            if jumlah_baru < 1 or jumlah_baru > 99:
                print(Fore.RED + "Jumlah barang harus antara 1 sampai 99.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid.")

    # Input harga barang dengan validasi angka dan batasan
    while True:
        try:
            harga_baru = int(input(Fore.GREEN + "Masukkan Harga Barang : " + Style.RESET_ALL))
            if harga_baru < 1 or harga_baru > 9999999:
                print(Fore.RED + "Harga barang harus antara 1 sampai 9.999.999.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid.")

    garis(panjang)
    yakin = input(Fore.GREEN + "Apakah Data Sudah Benar? (Y/N) : " + Style.RESET_ALL).strip().lower()
    if yakin == 'y':
        # Tambah data barang baru ke list struk
        struk.append({
            "id": id_baru.upper(),
            "tipe": tipe_baru,
            "barang": nama_baru,
            "jumlah": jumlah_baru,
            "harga": harga_baru
        })
        print(Fore.GREEN + "Barang Berhasil Ditambah Ke Dalam Struk")
        tampilkan_struk(struk)
    else:
        print(Fore.RED + "Penambahan barang dibatalkan.")

# Fungsi update data barang berdasarkan ID
def update_barang():
    id_edit = input(Fore.GREEN + "Masukkan ID Barang : " + Style.RESET_ALL).strip()
    barang_edit = cari_barang_by_id(id_edit)
    if not barang_edit:
        print(Fore.RED + "ID Barang Tidak Ditemukan.")
        return
    barang = barang_edit[0]

    tampilkan_struk([barang])  # Tampilkan data barang yang akan diedit

    yakin_update = input(Fore.GREEN + "Ketik Y jika ingin update atau N Jika Ingin Cancel Update (Y/N) : " + Style.RESET_ALL).strip().lower()
    if yakin_update != 'y':
        print(Fore.RED + "Update dibatalkan.")
        return

    kolom_edit = input(Fore.GREEN + "Masukkan Kolom yang Ingin di Edit\n(Tipe/Barang/Jumlah/Harga): " + Style.RESET_ALL).strip().lower()

    # Edit sesuai kolom yang dipilih
    if kolom_edit == "tipe":
        print("Pilih Tipe Barang:")
        for nomor, tipe in tipe_barang_dict.items():
            print(f"{nomor}. {tipe}")
        while True:
            try:
                pilihan_tipe = int(input(Fore.GREEN + "Masukkan nomor tipe barang: " + Style.RESET_ALL))
                if pilihan_tipe not in tipe_barang_dict:
                    print(Fore.RED + "Pilihan tipe barang tidak valid.")
                    continue
                barang["tipe"] = tipe_barang_dict[pilihan_tipe]
                break
            except ValueError:
                print(Fore.RED + "Masukkan angka yang valid.")
    elif kolom_edit == "barang":
        barang["barang"] = input(Fore.GREEN + "Masukkan Nama Barang Baru: " + Style.RESET_ALL).strip().title()
    elif kolom_edit == "jumlah":
        while True:
            try:
                jumlah_baru = int(input(Fore.GREEN + "Masukkan Jumlah Barang Baru: " + Style.RESET_ALL))
                if jumlah_baru < 1 or jumlah_baru > 99:
                    print(Fore.RED + "Jumlah barang harus antara 1 sampai 99.")
                    continue
                barang["jumlah"] = jumlah_baru
                break
            except ValueError:
                print(Fore.RED + "Masukkan angka yang valid.")
    elif kolom_edit == "harga":
        while True:
            try:
                harga_baru = int(input(Fore.GREEN + "Masukkan Harga Barang Baru: " + Style.RESET_ALL))
                if harga_baru < 1 or harga_baru > 9999999:
                    print(Fore.RED + "Harga barang harus antara 1 sampai 9.999.999.")
                    continue
                barang["harga"] = harga_baru
                break
            except ValueError:
                print(Fore.RED + "Masukkan angka yang valid.")
    else:
        print(Fore.RED + "Kolom tidak valid.")
        return

    yakin_simpan = input(Fore.GREEN + "Apakah Anda Ingin Update Data (Y/N): " + Style.RESET_ALL).strip().lower()
    if yakin_simpan == 'y':
        print(Fore.GREEN + "Update Data Berhasil")
        tampilkan_struk(struk)
    else:
        print(Fore.RED + "Update dibatalkan.")

# Fungsi menghapus barang berdasarkan ID
def hapus_barang():
    id_hapus = input(Fore.GREEN + "Masukkan ID Barang yang ingin dihapus: " + Style.RESET_ALL).strip()
    barang_hapus = cari_barang_by_id(id_hapus)
    if not barang_hapus:
        print(Fore.RED + "ID Barang Tidak Ditemukan.")
        return
    struk.remove(barang_hapus[0])  # Hapus barang dari list
    print(Fore.GREEN + "Barang Berhasil Dihapus")
    tampilkan_struk(struk)

# Fungsi utama program yang menjalankan loop menu utama
def main():
    while True:
        pilihan = tampilkan_menu_utama()
        if pilihan == '1':
            while True:
                pilihan_lihat = tampilkan_menu_lihat()
                if pilihan_lihat == '1':
                    tampilkan_struk(struk)  # Tampilkan semua barang
                elif pilihan_lihat == '2':
                    id_cari = input(Fore.GREEN + "Masukkan ID Barang yang ingin dicari: " + Style.RESET_ALL).strip()
                    hasil = cari_barang_by_id(id_cari)
                    if hasil:
                        tampilkan_struk(hasil)
                    else:
                        print(Fore.RED + "Data tidak ditemukan.")
                elif pilihan_lihat == '3':
                    break  # Kembali ke menu utama
                else:
                    print(Fore.RED + "Pilihan tidak valid.")
        elif pilihan == '2':
            while True:
                pilihan_tambah = tampilkan_menu_tambah()
                if pilihan_tambah == '1':
                    tambah_barang()  # Tambah barang baru
                elif pilihan_tambah == '2':
                    break
                else:
                    print(Fore.RED + "Pilihan tidak valid.")
        elif pilihan == '3':
            while True:
                pilihan_edit = tampilkan_menu_edit()
                if pilihan_edit == '1':
                    update_barang()  # Update barang
                elif pilihan_edit == '2':
                    break
                else:
                    print(Fore.RED + "Pilihan tidak valid.")
        elif pilihan == '4':
            while True:
                pilihan_hapus = tampilkan_menu_hapus()
                if pilihan_hapus == '1':
                    hapus_barang()  # Hapus barang
                elif pilihan_hapus == '2':
                    break
                else:
                    print(Fore.RED + "Pilihan tidak valid.")
        elif pilihan == '5':
            print(Fore.GREEN + "Terima Kasih Sudah Menggunakan Program Ini.")
            break  # Keluar program
        else:
            print(Fore.RED + "Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
