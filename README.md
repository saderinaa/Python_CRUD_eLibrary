# 🔹 Python CRUD Application for E-Library

Aplikasi Python untuk mengelola **sistem perpustakaan digital** dengan operasi Create, Read, Update, dan Delete (CRUD).

---

## 🔹 Pemahaman Bisnis
E-Library adalah aplikasi digital untuk mengelola eBook bagi anggota terdaftar. Sistem ini memudahkan anggota meminjam eBook, mengusulkan buku baru, dan melihat koleksi. Admin dapat menyaring usulan buku dan mengawasi aktivitas anggota.

**Manfaat:**

* Manajemen eBook dan peminjaman terorganisir.
* Penanganan usulan buku oleh anggota lebih efisien.
* Dashboard admin untuk approve/reject usulan buku.
* Antarmuka mudah digunakan oleh anggota dan admin.

---

## 🔹 Sasaran Pengguna

* **Anggota:** Bisa registrasi, pinjam eBook, mengusulkan buku, dan melihat eBook yang dipinjam.
* **Admin / Pustakawan:** Bisa approve/reject usulan buku dan memantau semua usulan.
* **Non-anggota:** Bisa melihat daftar eBook dan info perpustakaan, tetapi akses penuh hanya setelah registrasi menjadi anggota.

---

## 🔹 Fitur

**Create:**

* Registrasi anggota baru.
* Usulkan eBook baru.

**Read:**

* Lihat daftar eBook.
* Lihat eBook yang dipinjam anggota.
* Lihat usulan eBook.
* Info perpustakaan dan kontak.

**Update:**

* Admin dapat approve/reject usulan eBook.

**Delete:**

* Anggota dapat menghapus usulan eBook yang masih pending.

---

## 🔹 Struktur Data

| Variabel          | Tipe Data | Keterangan                                              |
| ----------------- | --------- | ------------------------------------------------------- |
| `members`         | list      | Daftar anggota dengan code, name, email, phone, address |
| `ebooks`          | list      | Koleksi eBook (title, author)                           |
| `borrowed_books`  | dict      | Buku yang dipinjam oleh anggota (key: kode anggota)     |
| `suggested_books` | list      | Buku yang diusulkan anggota dengan status dan pengusul  |
| `admins`          | list      | Data admin untuk login                                  |

---

## 🔹 Data Dummy Contoh

**Anggota:**

| Kode | Nama  | Email                                     | Telepon      | Alamat   |
| ---- | ----- | ----------------------------------------- | ------------ | -------- |
| B01  | Andi  | [andi@email.com](mailto:andi@email.com)   | 08123456789  | Jakarta  |
| B02  | Budi  | [budi@email.com](mailto:budi@email.com)   | 082233445566 | Bandung  |
| B03  | Citra | [citra@email.com](mailto:citra@email.com) | 083344556677 | Surabaya |

**eBooks:**

| Judul           | Penulis       |
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

## 🔹 Instalasi

**Persyaratan:** Python 3.7

---

## 🔹 Penggunaan

**Jalankan aplikasi:**

```bash
python main.py
```

**Operasi CRUD:**

* **Create:** Registrasi anggota, usulkan eBook.
* **Read:** Lihat daftar eBook, eBook yang dipinjam, usulan buku, info perpustakaan.
* **Update:** Admin approve/reject usulan eBook.
* **Delete:** Anggota hapus usulan buku yang pending.

---

## 🔹 Contoh Interaksi

```text
Selamat datang di Sistem Perpustakaan Digital!
1. Menu Member
2. Registrasi Member
3. Lihat eBook
4. Login Admin
5. Info Perpustakaan
6. Keluar

Pilih menu: 2
Masukkan nama: Dedi
Masukkan email: dedi@email.com
Masukkan nomor telepon: 081122334455
Masukkan alamat: Jakarta
Member 'Dedi' berhasil didaftarkan dengan kode B04!

Pilih menu: 1
Masukkan email member: dedi@email.com
Selamat datang, Dedi!
1. Lihat eBook
2. Pinjam eBook
3. Lihat eBook yang dipinjam
4. Usulkan Buku
5. Lihat Usulan Buku
6. Hapus Usulan Saya
7. Logout
```
