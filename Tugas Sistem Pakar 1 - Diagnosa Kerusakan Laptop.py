database_kerusakan = {
    "RAM Rusak":{"blue_screen", "sering_restart", "hang_lambat", "program_crash"},
    "Overheat (Prosesor)":{"panas_berlebih", "mati_mendadak", "sering_restart", "kipas_keras"},
    "VGA / GPU Bermasalah":{"artefak_layar", "no_display", "blue_screen", "program_crash"},
    "Hardisk Corrupt/Rusak":{"hdd_bunyi", "file_corrupt", "hang_lambat", "sering_restart"},
    "Power Supply (PSU) Rusak":{"tidak_menyala", "mati_mendadak", "sering_restart", "kipas_keras"}
}

solusi_kerusakan = {
    "RAM Rusak":
        "Lepas dan pasang kembali RAM. Bersihkan pin RAM dengan penghapus karet.\n"
        "\tCoba satu keping RAM saja untuk mengisolasi masalah.",
    "Overheat (Prosesor)":
        "Bersihkan kipas dan ventilasi dari debu.\n"
        "\tJika perlu, ganti thermal paste atau gunakan cooling pad.",
    "VGA / GPU Bermasalah":
        "Coba pasang ulang kartu VGA. Perbarui atau instal ulang driver grafis.\n"
        "\tCoba hubungkan ke monitor lain untuk memastikan.",
    "Hardisk Corrupt/Rusak":
        "Jalankan 'chkdsk /f /r' di CMD (Windows). Segera backup data penting.\n"
        "\tGanti hardisk jika terdengar suara klik terus-menerus.",
    "Power Supply (PSU) Rusak":
        "Periksa semua kabel daya sudah terpasang rapat. Uji dengan PSU lain.\n"
        "\tGanti PSU jika tegangan tidak stabil."
}

semua_gejala = [
    ("blue_screen","Apakah komputer sering muncul layar biru (Blue Screen)?"),
    ("sering_restart","Apakah komputer sering restart sendiri tiba-tiba?"),
    ("mati_mendadak","Apakah komputer mati mendadak tanpa peringatan?"),
    ("panas_berlebih","Apakah komputer/laptop terasa sangat panas saat dipakai?"),
    ("kipas_keras","Apakah suara kipas terdengar sangat keras atau berisik?"),
    ("hang_lambat","Apakah komputer sering hang atau berjalan sangat lambat?"),
    ("artefak_layar","Apakah muncul garis atau warna aneh di layar?"),
    ("no_display","Apakah layar blank/hitam meski komputer menyala?"),
    ("hdd_bunyi","Apakah terdengar suara klik atau gerinda dari dalam komputer?"),
    ("file_corrupt","Apakah ada file yang tiba-tiba rusak atau tidak bisa dibuka?"),
    ("tidak_menyala","Apakah komputer tidak menyala sama sekali saat power ditekan?"),
    ("program_crash","Apakah program sering menutup sendiri secara tiba-tiba?")
]

#FUNGSI TANYA GEJALA
gejala_pasien = []
def tanya_gejala(kode, pertanyaan):
    jawaban=input(f"  {pertanyaan} (y/t): ").strip().lower()
    if jawaban=="y":
        gejala_pasien.append(kode)

#MESIN INFERENSI
def diagnosa_kerusakan(gejala):
    hasil = []
    for kerusakan, gejala_syarat in database_kerusakan.items():
        if(gejala_syarat.issubset(gejala)):
            hasil.append(kerusakan)
    return hasil

#FUNGSI TAMPILKAN HASIL
def tampilkan_hasil(gejala):
    print("\nHASIL DIAGNOSA")

    hasil = diagnosa_kerusakan(gejala)
    if hasil:
        print(f"Gejala yang Anda alami  : {', '.join(gejala)}")
        print(f"Kerusakan terdeteksi    : {len(hasil)} kerusakan\n")
        for i, nama in enumerate(hasil, 1):
            print(f"{i}. {nama}")
            print(f"Solusi: {solusi_kerusakan[nama]}")
            print()
    else:
        print("Tidak terdeteksi kerusakan spesifik.")
        print("Coba restart komputer, perbarui driver,")
        print("atau konsultasikan ke teknisi.")

# PROGRAM UTAMA
def main():
    print("SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER")
    print("Jawab setiap pertanyaan dengan y (ya) atau t (tidak).\n")

    for kode, pertanyaan in semua_gejala:
        tanya_gejala(kode, pertanyaan)
    tampilkan_hasil(gejala_pasien)

if __name__ == "__main__":
    main()