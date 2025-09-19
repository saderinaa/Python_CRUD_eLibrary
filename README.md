# 📚 E-Library Python CRUD Application
Aplikasi Python untuk mengelola eBook dengan fitur CRUD untuk anggota dan admin.

## 🔹 Deskripsi

E-Library adalah aplikasi sederhana untuk **mengelola buku digital**. Sistem ini dirancang untuk **anggota terdaftar** yang ingin meminjam eBook, mengusulkan buku baru, dan melihat daftar eBook yang mereka pinjam. Non-anggota hanya bisa melihat daftar eBook dan info perpustakaan.

---

## 🔹 Sasaran Pengguna

* **Anggota:** Bisa pinjam eBook, mengusulkan buku, dan melihat eBook yang dipinjam.  
* **Admin / Pustakawan:** Bisa approve/reject usulan buku dan melihat semua usulan.  
* **Non-anggota:** Bisa melihat daftar eBook dan info perpustakaan, tapi akses penuh hanya setelah registrasi menjadi anggota.

---

## 🔹 Fitur

* **Registrasi Member:** Mendaftarkan pengguna baru menjadi anggota.  
* **Login Member:** Masuk ke dashboard anggota untuk mengakses fitur eBook.  
* **Lihat eBook:** Menampilkan seluruh koleksi eBook.  
* **Pinjam eBook:** Meminjam eBook untuk anggota terdaftar.  
* **Usulkan Buku:** Member bisa mengusulkan buku baru untuk ditambahkan.  
* **Hapus Usulan:** Member bisa menghapus usulan buku yang masih pending.  
* **Admin Approve/Reject:** Admin dapat menyetujui atau menolak usulan buku.  
* **Info Perpustakaan:** Menampilkan info layanan dan kontak perpustakaan.

---

## 🔹 Struktur Data

| Variabel          | Tipe Data | Keterangan                                |
| ----------------- | --------- | ----------------------------------------- |
| `suggested_books` | list      | Daftar buku usulan dari anggota           |
| `borrowed_books`  | dict      | Data peminjaman eBook (key: kode anggota) |
| `members`         | list      | Daftar anggota terdaftar                  |
| `ebooks`          | list      | Koleksi eBook (dictionary: title, author) |
| `admins`          | list      | Data admin untuk login                    |

---

## 🔹 Data Dummy Contoh

**Anggota:**

| Kode | Nama  | Email                                     | Telepon      | Alamat   |
| ---- | ----- | ----------------------------------------- | ------------ | -------- |
| B01  | Andi  | [andi@email.com](mailto:andi@email.com)   | 08123456789  | Jakarta  |
| B02  | Budi  | [budi@email.com](mailto:budi@email.com)   | 082233445566 | Bandung  |
| B03  | Citra | [citra@email.com](mailto:citra@email.com) | 083344556677 | Surabaya |

**eBook:**

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


