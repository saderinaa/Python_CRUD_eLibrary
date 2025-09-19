# 📚 E-Library Python CRUD Application
Aplikasi Python untuk mengelola eBook dengan fitur CRUD untuk anggota dan admin.

## 🔹 Sasaran Pengguna

* **Member / Anggota:** Dapat melihat, meminjam, mengusulkan, dan menghapus usulan eBook.
* **Admin:** Mengelola dan menyetujui atau menolak usulan eBook.

## 🔹 Fitur

### Member

* **Registrasi:** Mendaftar menjadi anggota.
* **Login:** Akses dashboard anggota.
* **Lihat eBook:** Melihat daftar eBook yang tersedia.
* **Pinjam eBook:** Meminjam eBook.
* **Usulkan Buku:** Menambahkan usulan eBook baru.
* **Lihat Usulan:** Melihat usulan eBook.
* **Hapus Usulan Saya:** Menghapus usulan eBook yang masih pending.

### Admin

* **Login Admin:** Masuk ke dashboard admin.
* **Lihat Semua Usulan:** Melihat daftar semua usulan eBook.
* **Approve/Reject Usulan:** Menyetujui atau menolak usulan eBook.

### Informasi Perpustakaan

* Peminjaman eBook: 7 hari per buku.
* Buku bisa dibaca online selama periode peminjaman.
* Bantuan & Kontak: [library@example.com](mailto:library@example.com) / 123-456-7890 (Senin-Jumat 08:00-16:00)

## 🔹 Instalasi

1. **Prerequisites:**

   * Python 3.13.5

2. **Jalankan aplikasi:**

```bash
python main.py
```

## 🔹 Data Model

* **Members / Anggota:** `code`, `name`, `email`, `phone`, `address`
* **eBooks:** `title`, `author`
* **Admins:** `email`, `password`
* **Borrowed Books:** Dictionary dengan `member code` sebagai key, list eBook sebagai value.
* **Suggested Books:** List eBook yang diusulkan dengan status (`pending`, `approve`, `reject`).

