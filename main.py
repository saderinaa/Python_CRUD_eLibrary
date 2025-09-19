# ===================================
# E-Library Program
# ===================================
# Developed by: Shadrina Putri Nabila
# JCDSBSDAM29
# ===================================

# ===== Collection Data Types =====
suggested_books = []
borrowed_books = {}
members = [
    {
        "code": "B01",
        "name": "Andi",
        "email": "andi@email.com",
        "phone": "08123456789",
        "address": "Jakarta"
    },
    {
        "code": "B02",
        "name": "Budi",
        "email": "budi@email.com",
        "phone": "082233445566",
        "address": "Bandung"
    },
    {
        "code": "B03",
        "name": "Citra",
        "email": "citra@email.com",
        "phone": "083344556677",
        "address": "Surabaya"
    }
]

ebooks = [
    {"title": "Bumi", "author": "Tere Liye"},
    {"title": "Bulan", "author": "Tere Liye"},
    {"title": "Matahari", "author": "Tere Liye"},
    {"title": "Rindu", "author": "Tere Liye"},
    {"title": "Ayah", "author": "Andrea Hirata"},
    {"title": "Laskar Pelangi", "author": "Andrea Hirata"},
    {"title": "Negeri 5 Menara", "author": "Ahmad Fuadi"},
    {"title": "Ranah 3 Warna", "author": "Ahmad Fuadi"},
    {"title": "Dilan 1990", "author": "Pidi Baiq"},
    {"title": "Dilan 1991", "author": "Pidi Baiq"}
]

admins = [
    {"email": "admin@perpus.com", "password": "admin123"}
]


# ===== Member Registration =====
def member_regist():
    print("\n=== Registrasi Member ===")
    code = f"B{len(members)+1:02d}"
    name = input("Masukkan nama: ").title()
    email = input("Masukkan email: ").lower()
    phone = input("Masukkan nomor telepon: ")
    address = input("Masukkan alamat: ").title()

    # cek email unik
    for member in members:
        if member["email"] == email:
            print("Email sudah terdaftar, gunakan email lain!\n")
            return

    members.append({
        "code": code,
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    })
    print(f"Member '{name}' berhasil didaftarkan dengan kode {code}!\n")


# ===== Member Login & Dashboard =====
def member_menu():
    email = input("Masukkan email member: ")
    for member in members:
        if member["email"] == email:
            print(f"Selamat datang, {member['name']}!")
            member_dashboard(member)
            return
    print("Email tidak ditemukan! Silakan registrasi dulu.\n")


def member_dashboard(member):
    while True:
        print(f"\n=== Dashboard Member ({member['name']}) ===")
        print("1. Lihat eBook")
        print("2. Pinjam eBook")
        print("3. Lihat eBook yang dipinjam")
        print("4. Usulkan Buku")
        print("5. Lihat Usulan Buku")
        print("6. Hapus Usulan Saya")
        print("7. Logout")

        choice = input("Pilih menu: ")

        if choice == "1":
            view_ebooks()
        elif choice == "2":
            borrow_ebooks(member)
        elif choice == "3":
            books = borrowed_books.get(member["code"], [])
            if not books:
                print("\nBelum ada buku yang dipinjam.\n")
            else:
                print("\n=== eBook yang dipinjam ===")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book['title']} - {book['author']}")
                print()
        elif choice == "4":
            suggest_ebook(member)
        elif choice == "5":
            view_suggestions()
        elif choice == "6":
            delete_my_suggestion(member)
        elif choice == "7":
            print("Logout...\n")
            break
        else:
            print("Pilihan tidak valid!\n")


# ===== eBook Features =====
def view_ebooks():
    print("\n=== Daftar eBook ===")
    for i, ebook in enumerate(ebooks, 1):
        print(f"{i}. {ebook['title']} - {ebook['author']}")
    print()


def borrow_ebooks(member):
    print("\n=== Pinjam eBook ===")
    for i, ebook in enumerate(ebooks, 1):
        print(f"{i}. {ebook['title']} - {ebook['author']}")

    choice = input("Masukkan nomor buku yang ingin dipinjam: ")
    if choice.isdigit():
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(ebooks):
            book = ebooks[selected_index]
            if member["code"] not in borrowed_books:
                borrowed_books[member["code"]] = []
            borrowed_books[member["code"]].append(book)
            print(f"Buku '{book['title']}' berhasil dipinjam.\n")
        else:
            print("Nomor tidak valid!\n")
    else:
        print("Harap masukkan angka!\n")


# ===== Suggestion Features =====
def suggest_ebook(member):
    print("\n=== Usulkan eBook Baru ===")
    title = input("Masukkan judul buku: ").title()
    author = input("Masukkan nama penulis: ").title()

    while True:
        confirm = input("Simpan usulan ini? (y/n): ").lower()
        if confirm == "y":
            suggested_books.append({
                "title": title,
                "author": author,
                "suggested_by": member["name"],
                "status": "pending"
            })
            print(f"Usulan '{title}' oleh {author} berhasil disimpan (status: pending).\n")
            break
        elif confirm == "n":
            print("Usulan dibatalkan.\n")
            break
        else:
            print("Masukkan hanya 'y' atau 'n'!\n")


def view_suggestions():
    print("\n=== Daftar Usulan eBook ===")
    if not suggested_books:
        print("Belum ada usulan buku.\n")
    else:
        for i, ebook in enumerate(suggested_books, 1):
            print(f"{i}. {ebook['title']} - {ebook['author']} "
                  f"(diusulkan oleh {ebook['suggested_by']}, status: {ebook['status']})")
    print()


def delete_my_suggestion(member):
    print("\n=== Hapus Usulan Saya ===")
    my_suggestions = [
        s for s in suggested_books if s["suggested_by"] == member["name"] and s["status"] == "pending"
    ]

    if not my_suggestions:
        print("Tidak ada usulan yang bisa dihapus.\n")
        return

    for i, ebook in enumerate(my_suggestions, 1):
        print(f"{i}. {ebook['title']} - {ebook['author']} (status: {ebook['status']})")

    choice = input("Masukkan nomor usulan yang ingin dihapus (Enter untuk batal): ")
    if choice.isdigit():
        selected_index = int(choice) - 1
        if 0 <= selected_index < len(my_suggestions):
            to_remove = my_suggestions[selected_index]
            suggested_books.remove(to_remove)
            print(f"Usulan '{to_remove['title']}' berhasil dihapus.\n")
        else:
            print("Nomor tidak valid!\n")
    elif choice == "":
        print("Batal hapus.\n")
    else:
        print("Masukkan angka yang valid!\n")


# ===== Admin Features =====
def approve_reject():
    print("\n=== Menu Admin: Approve/Reject Usulan ===")
    pending_books = [b for b in suggested_books if b["status"] == "pending"]
    if not pending_books:
        print("\nBelum ada usulan buku untuk disetujui atau ditolak.\n")
        return

    print("\n=== Usulan Buku Pending ===")
    for i, book in enumerate(pending_books, 1):
        print(f"{i}. {book['title']} - {book['author']} (diusulkan oleh {book['suggested_by']})")

    choice = input("Masukkan nomor usulan yang ingin diubah status: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(pending_books):
            action = input("Approve atau Reject? (approve/reject): ").lower()
            if action in ["approve", "reject"]:
                pending_books[index]["status"] = action
                print(f"Usulan '{pending_books[index]['title']}' telah {action}.\n")
            else:
                print("Masukkan 'approve' atau 'reject'.\n")
        else:
            print("Nomor tidak valid!\n")
    else:
        print("Harap masukkan angka!\n")


def admin_dashboard():
    while True:
        print("\n=== Dashboard Admin ===")
        print("1. Lihat Semua Usulan")
        print("2. Approve/Reject Usulan")
        print("3. Logout")
        choice = input("Pilih menu: ")
        if choice == "1":
            view_suggestions()
        elif choice == "2":
            approve_reject()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid!\n")


def admin_login():
    print("\n=== Login Admin ===")
    email = input("Email: ")
    password = input("Password: ")
    for admin in admins:
        if admin["email"] == email and admin["password"] == password:
            print("Login berhasil.\n")
            admin_dashboard()
            return
    print("Email atau password salah.\n")


# ===== Info / Help =====
def library_info():
    print("\n************************************************************")
    print("*                 Informasi Perpustakaan                   *")
    print("************************************************************")
    print("* 1. Peminjaman e-Book:                                    *")
    print("*    - Setiap e-book dipinjam selama 7 hari.               *")
    print("*    - Setelah 7 hari, akses ditutup otomatis.             *")
    print("*    - Buku bisa dibaca online selama periode pinjam.      *")
    print("*                                                          *")
    print("* 2. Bantuan & Kontak:                                     *")
    print("*    - Email: library@example.com                          *")
    print("*    - Telepon: 123-456-7890                               *")
    print("*    - Layanan: Senin-Jumat, 08:00-16:00                   *")
    print("************************************************************")


# ===== Main Menu =====
def main_menu():
    print("=====================================================")
    print("=            Sistem Perpustakaan Digital            =")
    print("=====================================================")
    print("= 1. Menu Member                                    =")
    print("= 2. Registrasi Member                              =")
    print("= 3. Lihat eBook                                    =")
    print("= 4. Login Admin                                    =")
    print("= 5. Info Perpustakaan                              =")
    print("= 6. Keluar                                         =")
    print("=====================================================")


# ===== Program Loop =====
while True:
    main_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        member_menu()
    elif choice == "2":
        member_regist()
    elif choice == "3":
        view_ebooks()
    elif choice == "4":
        admin_login()
    elif choice == "5":
        library_info()
    elif choice == "6":
        print("Terima kasih! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!\n")
