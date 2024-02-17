from database.model import menuMakanan
from database.jalankan import create_engine_and_session

# Data yang akan dimasukkan ke dalam tabel
menu_data = [
    {"namaMenu": "Nasi putih", "jumlah": 100.0, "satuan": "gram", "jumlahKalori": 175.0},
    {"namaMenu": "Nasi merah", "jumlah": 100.0, "satuan": "gram", "jumlahKalori": 110.0},
    {"namaMenu": "Kentang rebus", "jumlah": 100.0, "satuan": "gram", "jumlahKalori": 87.0},
    {"namaMenu": "Ubi jalar", "jumlah": 100.0, "satuan": "gram", "jumlahKalori": 86.0},
    {"namaMenu": "Singkong", "jumlah": 100.0, "satuan": "gram", "jumlahKalori": 160.0},
    {"namaMenu": "Roti putih", "jumlah": 1.0, "satuan": "iris", "jumlahKalori": 66.0},
    {"namaMenu": "Roti gandum", "jumlah": 1.0, "satuan": "iris", "jumlahKalori": 67.0},
    {"namaMenu": "Mi goreng instan", "jumlah": 80.0, "satuan": "gram", "jumlahKalori": 350.0},
]

# Fungsi untuk memasukkan data ke dalam tabel
def insert_menu_data(session, menu_data):
    for data in menu_data:
        menu = menuMakanan(**data)
        menu.menuID = int(menuMakanan.generate_random_key())
        session.add(menu)
    session.commit()

# Membuat sesi
session = create_engine_and_session()

# Memasukkan data ke dalam tabel
insert_menu_data(session, menu_data)

# Menampilkan data dari tabel
all_menus = session.query(menuMakanan).all()

for menu in all_menus:
    print(f"Menu ID: {menu.menuID}, Nama: {menu.namaMenu}, Jumlah: {menu.jumlah} {menu.satuan}, Kalori: {menu.jumlahKalori} kkal")

# Menutup sesi
session.close()