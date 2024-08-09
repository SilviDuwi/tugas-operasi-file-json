import json
import os

class JsonKu:
    def __init__(self, filename):
        self.filename = filename
    
    def baca(self):
        """Membaca data dari file JSON"""
        if not os.path.isfile(self.filename):
            return "File tidak ditemukan"
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data
    
    def tulis(self, data):
        """Menulis data ke file JSON"""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        return "Data berhasil ditulis"
    
    def update(self, key, value):
        """Mengupdate nilai berdasarkan kunci"""
        data = self.baca()
        if isinstance(data, dict):
            data[key] = value
            self.tulis(data)
            return "Data berhasil diupdate"
        return "Data tidak valid untuk update"
    
    def delete(self, key):
        """Menghapus kunci dan nilainya dari file JSON"""
        data = self.baca()
        if isinstance(data, dict):
            if key in data:
                del data[key]
                self.tulis(data)
                return "Kunci berhasil dihapus"
            return "Kunci tidak ditemukan"
        return "Data tidak valid untuk dihapus"
