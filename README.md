# 📚 E-Library Python CRUD Application

## 🔹 Deskripsi

Aplikasi Python sederhana untuk mengelola perpustakaan digital dengan operasi Create, Read, Update, dan Delete (CRUD) pada buku dan anggota.

---

## 🔹 Tujuan Sistem

Sistem ini dirancang untuk perpustakaan internal (sekolah, kampus, komunitas) agar pengelolaan buku dan anggota lebih efisien. Anggota terdaftar dapat meminjam eBook dan mengusulkan buku baru, sementara non-anggota tidak dapat mengakses fitur ini.

**Manfaat:**

* Pengelolaan buku digital lebih mudah
* Pelacakan peminjaman anggota cepat dan jelas
* Pengelolaan usulan buku terstruktur

**Sasaran Pengguna:** Anggota Terdaftar dan Administrator/Pustakawan

---

## 🔹 Fitur

* **Create:**

  * Registrasi anggota baru
  * Usulkan eBook baru

* **Read:**

  * Lihat daftar eBook
  * Lihat eBook yang dipinjam
  * Lihat usulan buku

* **Update:**

  * Admin dapat approve/reject usulan buku

* **Delete:**

  * Anggota dapat menghapus usulan buku sendiri yang berstatus pending

---

## 🔹 Instalasi

**Persyaratan:**

* Python 3.13

---

## 🔹 Penggunaan

1. Jalankan aplikasi:

```bash
python main.py
```

2. Pilih menu utama untuk mengakses fitur: member, registrasi, lihat eBook, login admin, info perpustakaan, atau keluar.

---

## 🔹 Struktur Data

| Variabel          | Tipe Data | Keterangan                                |
| ----------------- | --------- | ----------------------------------------- |
| `suggested_books` | list      | Daftar buku yang diusulkan                |
| `borrowed_books`  | dict      | Data peminjaman eBook (key: code member)  |
| `members`         | list      | Daftar anggota terdaftar                  |
| `ebooks`          | list      | Koleksi eBook (dictionary: title, author) |
| `admins`          | list      | Daftar admin                              |

---

## 🔹 Data Dummy

**Anggota:**

| Code | Nama  | Email                                     | Phone        | Alamat   |
| ---- | ----- | ----------------------------------------- | ------------ | -------- |
| B01  | Andi  | [andi@email.com](mailto:andi@email.com)   | 08123456789  | Jakarta  |
| B02  | Budi  | [budi@email.com](mailto:budi@email.com)   | 082233445566 | Bandung  |
| B03  | Citra | [citra@email.com](mailto:citra@email.com) | 083344556677 | Surabaya |

**Buku:**

| Judul Buku      | Penulis       |
| --------------- | ------------- |
| Bumi            | Tere Liye     |
| Bulan           | Tere Liye     |
| Matahari        | Tere Liye     |
| Rindu           | Tere Liye     |
| Ayah            | Andrea Hirata |
| Laskar Pelangi  | Andrea Hirata |
| Negeri 5 Menara | Ahmad Fuadi   |
| Ranah 3 Warna   | Ahmad Fuadi   |
| Dilan 1990      | Pidi Baiq     |
| Dilan 1991      | Pidi Baiq     |

---

## 🔹 Contoh Interaksi

```text
Selamat datang di E-Library!
1. Menu Member
2. Registrasi Member
3. Lihat eBook
4. Login Admin
5. Info Perpustakaan
6. Keluar

Pilih menu: 1
Masukkan email member: andi@email.com
Selamat datang, Andi!

=== Dashboard Member ===
1. Lihat eBook
2. Pinjam eBook
3. Lihat eBook yang dipinjam
4. Usulkan Buku
5. Lihat Usulan Buku
6. Hapus Usulan Saya
7. Logout
```

