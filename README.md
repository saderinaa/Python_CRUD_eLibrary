# 📚 E-Library Python CRUD Application
---

## Deskripsi

Aplikasi Python sederhana untuk mengelola perpustakaan digital dengan operasi Create, Read, Update, dan Delete (CRUD) pada buku dan anggota.

---

## Business Understanding

Proyek ini dirancang untuk perpustakaan atau koleksi pribadi untuk memudahkan pengelolaan buku dan anggota. Manajemen yang efisien memastikan ketersediaan buku, pelacakan peminjaman, dan pengelolaan anggota yang baik.

**Manfaat:**

* Pengelolaan buku lebih efisien
* Pelacakan anggota dan peminjaman mudah
* Proses peminjaman cepat dan jelas
* Mempermudah pengawasan perpustakaan

**Sasaran Pengguna:** Administrator/Pustakawan dan Anggota Terdaftar.

---

## Fitur

* **Create (Tambah Buku/Anggota):** Menambahkan buku atau anggota baru dengan detail lengkap.
* **Read (Lihat Buku/Anggota):** Menampilkan daftar buku atau anggota, mencari berdasarkan ID, judul, atau nama.
* **Update:** Memperbarui data buku atau anggota sesuai kebutuhan.
* **Delete:** Menghapus buku atau anggota yang sudah tidak digunakan.

---

## Instalasi
Persyaratan:
Python 3.13
---

## Model Data

**Buku:**

* `id` (String, Unik)
* `title` (String)
* `author` (String)

**Anggota:**

* `name` (String)
* `email` (String, opsional)
* `borrowed_books` (List)

---

## Struktur Data

| Variabel          | Tipe Data | Keterangan                               |
| ----------------- | --------- | ---------------------------------------- |
| `suggested_books` | list      | Daftar buku rekomendasi                  |
| `borrowed_books`  | dict      | Data peminjaman buku (key: ID buku)      |
| `members`         | list      | Anggota terdaftar                        |
| `ebooks`          | list      | Koleksi buku (dictionary: title, author) |

---

## Data Dummy

| ID  | Judul Buku | Penulis   |
| --- | ---------- | --------- |
| B01 | Bumi       | Tere Liye |
| B02 | Bulan      | Tere Liye |
| B03 | Anak Badai | Tere Liye |

---

## Contoh Interaksi

```text
Selamat datang di E-Library!
1. Lihat Koleksi Buku
2. Tambah Buku
3. Pinjam Buku
4. Keluar

Daftar Buku Tersedia:
B01 - Bumi (Tere Liye)
B02 - Bulan (Tere Liye)
B03 - Anak Badai (Tere Liye)

Buku 'Bumi' berhasil dipinjam oleh Budi.
```
