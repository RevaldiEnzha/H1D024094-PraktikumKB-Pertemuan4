# Sistem Pakar Diagnosa Kerusakan Komputer

Program Python berbasis console yang menggunakan konsep sistem pakar untuk membantu mendiagnosa kemungkinan kerusakan komputer atau laptop berdasarkan gejala yang dialami pengguna.
Program akan menanyakan beberapa gejala, lalu mencocokkannya dengan data kerusakan yang sudah disimpan di dalam sistem.

---

## Fitur

- Mendeteksi **5 jenis kerusakan** komputer/laptop
- Berbasis **mesin inferensi** menggunakan struktur data Dictionary
- Menampilkan **solusi singkat** untuk setiap kerusakan yang terdeteksi
- Menangani kondisi ketika **gejala tidak cocok** dengan kerusakan manapun

---

## Struktur Program

### 1. Knowledge Base — `database_kerusakan`

```python
database_kerusakan = {
    "RAM Rusak": {"blue_screen", "sering_restart", "hang_lambat", "program_crash"},
    ...
}
```

Bagian ini menyimpan data kerusakan dan gejalanya. Jika semua gejala pada sebuah kerusakan terpenuhi, maka sistem akan menganggap kerusakan tersebut terdeteksi.

---

### 2. Basis Solusi — `solusi_kerusakan`

```python
solusi_kerusakan = {
    "RAM Rusak": "Lepas dan pasang kembali RAM. Bersihkan pin RAM dengan penghapus karet...",
    ...
}
```

Berisi solusi atau saran perbaikan untuk tiap kerusakan. Struktur datanya juga menggunakan dictionary, sehingga ketika sebuah kerusakan terdeteksi, program bisa langsung menampilkan solusi yang sesuai.

---

### 3. Daftar Pertanyaan Gejala — `semua_gejala`

```python
semua_gejala = [
    ("blue_screen", "Apakah komputer sering muncul layar biru (Blue Screen)?"),
    ...
]
```

Berisi **12 pertanyaan gejala** yang setiap data terdiri dari `(kode_gejala, teks_pertanyaan)`. Kode gejala digunakan sebagai penghubung antara jawaban pengguna dengan `database_kerusakan`.

---

### 4. Fungsi Input Gejala — `tanya_gejala()`

```python
def tanya_gejala(kode, pertanyaan):
    jawaban = input(f"  {pertanyaan} (y/t): ").strip().lower()
    if jawaban == "y":
        gejala_pasien.append(kode)
```

Menampilkan pertanyaan satu per satu ke pengguna. Jika pengguna menjawab `y`, kode gejala tersebut ditambahkan ke list `gejala_pasien`. List ini berisi semua gejala yang dialami oleh pengguna.

---

### 5. Mesin Inferensi — `diagnosa_kerusakan()`

```python
def diagnosa_kerusakan(gejala):
    hasil = []
    for kerusakan, gejala_syarat in database_kerusakan.items():
        if gejala_syarat.issubset(gejala):
            hasil.append(kerusakan)
    return hasil
```

Inti dari program. Fungsi ini membandingkan gejala pengguna dengan setiap aturan di `database_kerusakan`. Metode `.issubset()` memastikan bahwa **semua gejala yang disyaratkan** untuk suatu kerusakan harus terpenuhi agar kerusakan itu terdeteksi. Bisa mendeteksi lebih dari satu kerusakan sekaligus.

---

### 6. Fungsi Output — `tampilkan_hasil()`

```python
def tampilkan_hasil(gejala):
    hasil = diagnosa_kerusakan(gejala)
    if hasil:
        # tampilkan nama kerusakan dan solusinya
    else:
        # tampilkan pesan tidak terdeteksi
```

Menampilkan hasil diagnosa ke layar. Jika ada kerusakan yang cocok, program mencetak nama kerusakan beserta solusinya. Jika tidak ada yang cocok, program menampilkan saran umum untuk pengguna.

---

### 7. Fungsi Utama — `main()`

```python
def main():
    for kode, pertanyaan in semua_gejala:
        tanya_gejala(kode, pertanyaan)
    tampilkan_hasil(gejala_pasien)
```

Fungsi pengatur jalannya program. Mengiterasi seluruh daftar gejala, mengumpulkan jawaban pengguna, lalu memanggil fungsi tampil hasil.

---

## Cara Menjalankan

```bash
python "Tugas Sistem Pakar 1 - Diagnosa Kerusakan Laptop.py"
```

Jawab setiap pertanyaan dengan `y` (ya) atau `t` (tidak).

---

## Contoh Output

```
SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER
Jawab setiap pertanyaan dengan y (ya) atau t (tidak).

  Apakah komputer sering muncul layar biru (Blue Screen)? (y/t): y
  Apakah komputer sering restart sendiri tiba-tiba? (y/t): y
  ...

HASIL DIAGNOSA
Gejala yang Anda alami  : blue_screen, sering_restart, hang_lambat, program_crash
Kerusakan terdeteksi    : 1 kerusakan

1. RAM Rusak
Solusi: Lepas dan pasang kembali RAM. Bersihkan pin RAM dengan penghapus karet.
        Coba satu keping RAM saja untuk mengisolasi masalah.
```

---

## Kerusakan yang Dapat Dideteksi

| No | Kerusakan | Gejala yang Diperlukan |
|----|-----------|------------------------|
| 1 | RAM Rusak | Blue screen, sering restart, hang/lambat, program crash |
| 2 | Overheat (Prosesor) | Panas berlebih, mati mendadak, sering restart, kipas keras |
| 3 | VGA / GPU Bermasalah | Artefak layar, no display, blue screen, program crash |
| 4 | Hardisk Corrupt/Rusak | Bunyi HDD, file corrupt, hang/lambat, sering restart |
| 5 | Power Supply (PSU) Rusak | Tidak menyala, mati mendadak, sering restart, kipas keras |

---

## Requirement

- Python 3.x
- Tidak memerlukan library tambahan (hanya menggunakan built-in Python)
