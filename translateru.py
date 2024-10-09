import os
from googletrans import Translator

# Inisialisasi translator
translator = Translator()

# Tentukan direktori tempat file JSON berada
directory = "E:\Playground\RandomCode\Translatorfile\dump"


# Fungsi untuk menerjemahkan nama file
def translate_filename(filename):
    # Hilangkan ekstensi file agar tidak ikut diterjemahkan
    name, ext = os.path.splitext(filename)

    # Terjemahkan nama file dari Rusia ke Indonesia
    translated = translator.translate(name, src="ru", dest="id").text

    # Gabungkan kembali dengan ekstensi file
    new_filename = translated + ext
    return new_filename


# Loop melalui semua file di direktori
for filename in os.listdir(directory):
    if filename.endswith(".json"):  # Pastikan hanya file JSON yang diterjemahkan
        # Terjemahkan nama file
        new_filename = translate_filename(filename)

        # Ganti nama file
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        # Ubah nama file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("Semua file telah diterjemahkan dan diubah namanya.")
