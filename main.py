from json_1 import JsonKu  # Import class JsonKu dari file json_ku.py

def main():
    # Nama file JSON
    filename = 'data.json'
    
    # Inisialisasi objek JsonKu
    json_ku = JsonKu(filename)
    
    # Data awal yang akan ditulis ke file JSON
    data_awal = {
        "judul": "langit dan semesta",
        "pengarang": "silvi duwi nabila",
        "tahun_terbit": 2024
    }
    
    # Menulis data ke file
    print("Menulis data ke file:")
    print(json_ku.tulis(data_awal))  # Output: Data berhasil ditulis
    
    # Membaca data dari file
    print("\nMembaca data dari file:")
    data_baca = json_ku.baca()
    print(data_baca)  # Output: {'judul': 'Aku', 'pengarang': 'Andi M. Ahmad', 'tahun_terbit': 2005}
    
    # Memperbarui data (misalnya, tahun terbit menjadi 2020)
    print("\nMemperbarui data (tahun_terbit menjadi 2020):")
    print(json_ku.update('tahun_terbit', 2020))  # Output: Data berhasil diupdate
    
    # Membaca data setelah update
    print("\nMembaca data setelah update:")
    data_baca = json_ku.baca()
    print(data_baca)  # Output: {'judul': 'Aku', 'pengarang': 'Andi M. Ahmad', 'tahun_terbit': 2020}
    
    # Menghapus data (misalnya, menghapus kunci 'pengarang')
    print("\nMenghapus data (kunci 'pengarang'):")
    print(json_ku.delete('pengarang'))  # Output: Kunci berhasil dihapus
    
    # Membaca data setelah penghapusan
    print("\nMembaca data setelah penghapusan:")
    data_baca = json_ku.baca()
    print(data_baca)  # Output: {'judul': 'Aku', 'tahun_terbit': 2020}

if __name__ == "__main__":
    main()
