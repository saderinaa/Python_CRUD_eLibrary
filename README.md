# Python_CRUD_eLibrary

# E-Library Program

A comprehensive Python application for managing digital library data with Create, Read, Update, and Delete (CRUD) operations.  

## Business Understanding

Proyek ini dibuat untuk membantu pengelolaan perpustakaan digital dengan fitur peminjaman eBook, registrasi member, usulan buku baru, serta manajemen usulan oleh admin. Sistem ini mendukung proses digitalisasi perpustakaan agar lebih efisien, transparan, dan mudah diakses.

### Manfaat:
- **Kemudahan akses**: Member dapat meminjam eBook kapan saja secara online.  
- **Transparansi**: Usulan buku baru bisa dilihat oleh semua member dan dikelola admin.  
- **Efisiensi administrasi**: Admin dapat dengan cepat menyetujui atau menolak usulan buku.  
- **Data terstruktur**: Informasi member, eBook, dan usulan tersimpan dalam struktur data Python yang jelas.  

### Target Pengguna:
- **Member perpustakaan** yang ingin meminjam eBook atau mengusulkan buku baru.  
- **Admin perpustakaan** yang bertugas mengelola usulan dan mengawasi jalannya sistem.  

---

## Features

### Member
- **Registrasi Member**: Menambahkan data member baru dengan validasi email unik.  
- **Login Member**: Mengakses dashboard pribadi berdasarkan email terdaftar.  
- **Pinjam eBook**: Memilih dan meminjam buku digital dari daftar yang tersedia.  
- **Lihat eBook yang Dipinjam**: Mengecek daftar eBook yang sedang dipinjam.  
- **Usulkan Buku**: Memberikan saran buku baru yang ingin ditambahkan ke perpustakaan.  
- **Lihat Usulan Buku**: Melihat daftar usulan buku yang diajukan oleh semua member.  
- **Hapus Usulan Saya**: Menghapus usulan yang statusnya masih pending.  

### Admin
- **Login Admin**: Akses khusus untuk admin dengan email dan password.  
- **Lihat Semua Usulan**: Menampilkan daftar usulan dari seluruh member.  
- **Approve/Reject Usulan**: Menyetujui atau menolak usulan buku dengan status update otomatis.  

### Info Perpustakaan
- Informasi umum mengenai aturan peminjaman eBook (misalnya durasi pinjam 7 hari).  
- Kontak layanan perpustakaan (email dan telepon).  

---

## Dummy Data

Untuk keperluan testing, program ini menggunakan data dummy:

- **Members**
  - B01 - Andi | andi@email.com | Jakarta  
  - B02 - Budi | budi@email.com | Bandung  
  - B03 - Citra | citra@email.com | Surabaya  

- **E-Books**
  - Bumi – Tere Liye  
  - Bulan – Tere Liye  
  - Matahari – Tere Liye  
  - Rindu – Tere Liye  
  - Ayah – Andrea Hirata  
  - Laskar Pelangi – Andrea Hirata  
  - Negeri 5 Menara – Ahmad Fuadi  
  - Ranah 3 Warna – Ahmad Fuadi  
  - Dilan 1990 – Pidi Baiq  
  - Dilan 1991 – Pidi Baiq  

- **Admin**
  - Email: `admin@perpus.com`  
  - Password: `admin123`  

- **Suggested Books**
  - Kosong secara default, akan terisi jika member memberikan usulan.  

---

## Installation

### Prasyarat:
- Python 3.7 atau lebih baru  

### Cara Menjalankan:
1. Clone repositori ini  
   ```bash
   git clone https://github.com/<your-username>/elibrary-program.git
   cd elibrary-program
   ```
2. Jalankan program:  
   ```bash
   python main.py
   ```

---

## Usage

Setelah program dijalankan, menu utama akan muncul dengan pilihan:  

1. Menu Member → login untuk akses dashboard member.  
2. Registrasi Member → menambahkan member baru.  
3. Lihat eBook → menampilkan daftar eBook yang tersedia.  
4. Login Admin → masuk sebagai admin untuk mengelola usulan.  
5. Info Perpustakaan → menampilkan informasi umum & kontak.  
6. Keluar → menghentikan program.  

---

## Data Model

Program ini menggunakan struktur **Collection Data Types (Python)**:  

- `members` → list of dict, menyimpan data member (code, name, email, phone, address).  
- `ebooks` → list of dict, menyimpan data eBook (title, author).  
- `borrowed_books` → dict, menyimpan daftar eBook yang dipinjam per member.  
- `suggested_books` → list of dict, menyimpan usulan buku dari member.  
- `admins` → list of dict, menyimpan akun admin (email, password).  

---
