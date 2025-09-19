# 📚 E-Library Program

**Developed by:** Shadrina Putri Nabil

**Class:** JCDSBSDAM29

---

## 🔹 **Deskripsi**

E-Library adalah aplikasi sederhana untuk mengelola buku digital, dirancang agar pengguna dapat dengan mudah menambah, melihat, dan meminjam buku.
Program ini membantu mengatur koleksi buku dan transaksi peminjaman secara efisien.

Pengguna dapat:

* Menambahkan buku baru ke koleksi
* Melihat daftar buku yang tersedia
* Meminjam buku
* Mengelola anggota dan transaksi peminjaman

---

## 🔹 **Fitur**

* **Tambah Buku:** Menambahkan buku ke koleksi.
* **Daftar Buku:** Menampilkan seluruh buku yang tersedia.
* **Peminjaman Buku:** Meminjam buku oleh anggota.
* **Data Anggota:** Menyimpan informasi anggota terdaftar.

---

## 🔹 **Struktur Data**

| Variabel          | Tipe Data | Keterangan                               |
| ----------------- | --------- | ---------------------------------------- |
| `suggested_books` | list      | Daftar buku rekomendasi                  |
| `borrowed_books`  | dict      | Data peminjaman buku (key: ID buku)      |
| `members`         | list      | Anggota terdaftar                        |
| `ebooks`          | list      | Koleksi buku (dictionary: title, author) |

---

## 🔹 **Data Dummy Contoh**

| ID  | Judul Buku | Penulis   |
| --- | ---------- | --------- |
| B01 | Bumi       | Tere Liye |
| B02 | Bulan      | Tere Liye |
| B03 | Anak Badai | Tere Liye |

---

## 🔹 **Contoh Interaksi**

```text
Selamat datang di E-Library!
1. Lihat Koleksi Buku
2. Tambah Buku
3. Pinjam Buku
4. Keluar

Pilih menu: 1
Daftar Buku Tersedia:
B01 - Bumi (Tere Liye)
B02 - Bulan (Tere Liye)
B03 - Anak Badai (Tere Liye)

Pilih menu: 3
Masukkan ID Buku: B01
Masukkan Nama Anggota: Budi
Buku 'Bumi' berhasil dipinjam oleh Budi.
```

---
