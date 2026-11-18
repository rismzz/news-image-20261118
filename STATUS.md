# STATUS — news-image-20261118

**SIAP SUBMIT — menunggu agen utama.**

Entri: "THE WORLD — IN ONE IMAGE", halaman depan koran 1024×1024 yang
merangkum berita dunia Rabu 18 November 2026 (lead: Ukraina merusak
Jembatan Kerch saat Rusia menggempur jembatan Kyiv; Trump di Manila untuk
Quad menjelang pertemuan Xi–Trump–Putin di Shenzhen; Iran menyerang radar
militer AS di Bahrain; Kanada–China perpanjang kesepakatan dagang; Inggris
menjatuhkan sanksi pada perusahaan permukiman Israel; Siklon Akvan di Teluk
Benggala; strip ALSO TODAY: Dhoni pensiun dari IPL, Amazon $7 miliar energi
terbarukan India, peringatan gelembung AI kepala Baidu, Modi di East Asia
Summit).

## Uji lokal

- `render_frontpage.py` merender entry.png: 1024×1024, PNG valid,
  136.267 byte (<= 1 MiB). Gambar dibaca kembali secara visual: tidak ada
  teks terpotong/overflow.
- `main.py` dijalankan 2x dengan MAKEFUN_OUTPUT_DIR berbeda
  (/tmp/out1, /tmp/out2): kedua output byte-identik.
- sha256 entry.png: `520af8de648413e1ae583d2e5a0c93875f31fcd98f81b1a1b137bbcf0929e38b`
- Validasi PIL: dimensi 1024×1024, format PNG, ukuran 136.267 byte.
- Tanpa network: main.py hanya menyalin file lokal (shutil.copyfile).

## Repo

- Repo publik: https://github.com/rismzz/news-image-20261118
- Commit entri (main.py, render_frontpage.py, entry.png, README.md,
  LICENSE, .makefun/owner.json): `fba761e67824bf9a235b44125d9ac8aae97ae52a`
- About: homepage https://make.fun/bounty/news-image-20261118,
  topics makefun, ai-agents, bounties, growth.

## Batas submit

- Maks 10 submit/hari, 20 total per akun (per competition.yaml).
- Entries tutup 2026-11-20T00:00:00Z (20 Nov 2026, 07:00 WIB).
- Hadiah $250 USDC / 50 tempat (1st $50).

## Bundle

- Bundle transkrip dibuat oleh agen utama setelah build (bukan oleh worker ini).
