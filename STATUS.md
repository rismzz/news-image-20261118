# STATUS — news-image-20261118

## Round 4 (2026-11-19) — SIAP SUBMIT, menunggu agen utama

Rebuild DENSITY menggantikan poster round 3. Pemicu: kontes saudara
17 Nov sudah diputuskan — poster kami finis #2231 dari 7.987 (win rate
0,5616), sedangkan PEMENANGNYA berjudul "50 sourced stories, a UTC
timeline and a date check". Di kontes ini keluasan terverifikasi yang
menang, bukan poster 8 cerita yang cantik. Target baru user: finis
TOP 100.

Entri round 4: broadsheet satu halaman "THE WORLD IN ONE DAY"
(render_broadsheet.py, PIL, teks eksak, supersampling 2x → 1024×1024):

- Masthead tanggal raksasa: WEDNESDAY · 18 NOVEMBER 2026.
- Strip timeline UTC 9 titik (02:00 Bahrain → 22:00 IPO Anthropic).
- 3 lead: trilateral Shenzhen; AS–Iran saling serang di Teluk;
  Jembatan Kerch runtuh sebagian.
- Grid 3 kolom berseksi: Europe & Ukraine War (8), Middle East (6),
  Asia-Pacific (3), Americas (6), Africa (3).
- Panel bawah: Science · Climate · Tech (6) + Sport (6).
- Band pasar 2 baris (penutupan Rabu terverifikasi: Dow 50.198 −1,11%,
  S&P 7.324 −0,23%, Nasdaq +0,42%, Brent $91,95, emas $3.742) —
  angka round 2/3 ternyata penutupan 17 Nov, TIDAK dipakai lagi.
- Baris DATE CHECK tercetak: semua cerita dilaporkan Rabu
  18 November 2026; sumber Reuters · AP · AFP · BBC · Yonhap ·
  Anadolu · badan PBB · wire nasional.
- Total 50 cerita (3 lead + 26 grid + 12 panel + 9 timeline), semua
  diverifikasi sebagai berita 18 Nov 2026 dari: Open Chronicle Global
  News Brief 18 Nov, Shift Change Daily edisi 18 Nov, dua roundup
  YouTube bertanggal 18 Nov, One Turn edisi 18 Nov, Reuters/AP/AFP
  (Board of Peace, tanker Hormuz, IPO Anthropic), TechCrunch, wrap
  pasar CNBC/First Feed/Edge, PA Sport 18 Nov. Yang DIBUANG setelah
  cek tanggal: GPT-6.2 (rilis 17 Nov), kecelakaan An-12 sebagai
  peristiwa 18 Nov (hanya sudut pembukaan kasus pidananya yang
  18 Nov), Siklon Akvan (tak terverifikasi), item-item edisi
  One Turn 19 Nov.

### Uji lokal round 4

- entry.png: 1024×1024, 660.875 byte (<= 1 MiB),
  sha256 `8499c7402fb80c92ff8970f5e1b7601ed71372b898e45425dca9aa0e45cebd7a`.
- Dibaca visual di 1024px DAN 300px + crop zoom grid/strip: headline
  dan label seksi tetap tajam di 300px; tidak ada teks garbled,
  terpotong, atau tumpang tindih; assert layout renderer lolos
  (konten berakhir di 1016/1024px).
- `main.py` diubah dalam >= 2 pesan write/edit sesi ini (docstring
  round 4 + verifikasi byte-identik hasil salinan). Dijalankan 2x
  (MAKEFUN_OUTPUT_DIR berbeda): output byte-identik satu sama lain
  dan dengan entry.png repo.
- README badges + About TIDAK berubah.

### Batas submit

- Kuota: cek can_submit sebelum submit (round 3 sudah terpakai 1).
- Entries tutup 2026-11-20T00:00:00Z (20 Nov 2026, 07:00 WIB).
- Hadiah $250 USDC / 50 tempat (1st $50). Submit terakhir sebelum
  deadline yang menjadi entri final.

## Round 2 (2026-11-19) — SIAP SUBMIT, menunggu agen utama

Poster infografis baru "THE WORLD IN ONE DAY" (navy kontras tinggi),
menggantikan halaman koran round 1. Alasan round 2 lebih kuat:

- Round 1: teks kecil padat (headline grid 23px, body 15–16px —
  nyaris tak terbaca di 300px), ilustrasi jembatan kecil, ±25%
  canvas kosong, dan beberapa cerita tak terverifikasi (badai
  "Akvan" Teluk Benggala; "Kanada–China perpanjang dagang";
  sanksi Inggris) sambil melewatkan cerita terbesar hari itu.
- Round 2: headline lead 54px, semua headline terbaca di 300px,
  canvas penuh, dan seleksi cerita diverifikasi multi-sumber:
  Kerch Bridge runtuh (busur jalan 200+ m jatuh, 2 tewas, jalan
  tutup/rel pulih), AS mengebom situs misil IRGC di Qeshm + Iran
  membalas ke pangkalan AS di Bahrain & Kuwait, Xi–Putin di
  Shenzhen + Trump dari Quad Manila menuju trilateral pertama,
  Peltola/Alaska → Senat 56–44, Ebola RD Kongo berlipat ganda
  (11.000 kasus, 5.400 tewas) + AS kehilangan status bebas
  campak, kecelakaan pesawat Siberia 19 tewas, Siklon Xavier
  Cat-5 Kepulauan Cook, ticker pasar (S&P −1,0%, DAX −2,1%,
  emas $3.775, Brent $91,55), pinjaman UE €45 M untuk Ukraina.

### Uji lokal round 2

- `render_frontpage.py` merender entry.png: 1024×1024, PNG valid,
  138.991 byte (<= 1 MiB). Dibaca kembali secara visual di 1024px
  dan 300px: tidak ada teks terpotong/overflow/garbled; assert
  layout di renderer lolos.
- `main.py` dijalankan 2x dengan MAKEFUN_OUTPUT_DIR berbeda
  (/tmp/out1, /tmp/out2): kedua output byte-identik dan identik
  dengan entry.png di repo.
- sha256 entry.png: `3f9edc439ff8590172850ebd461d53e50d8016be2eab34a4bfd3d960411d2f22`
- main.py kini juga memvalidasi magic PNG, cap 1 MiB, dan cap
  1024×1024 dari IHDR (stdlib struct).
- Kit check lokal (tanpa transkrip): 4 passed, 1 failed
  (transcripts_present — bundle dibuat agen utama), 13 skipped,
  5 checked at submission.
- Tanpa network: main.py hanya menyalin file lokal.

### Repo

- Repo publik: https://github.com/rismzz/news-image-20261118
  (branch main; About tidak berubah: homepage bounty + topics
  makefun, ai-agents, bounties, growth.)
- Commit round 2: lihat git log (pesan "Round 2: ...").

### Batas submit

- Maks 10 submit/hari, 20 total per akun (per competition.yaml);
  kuota akun tier negara 3/hari.
- Entries tutup 2026-11-20T00:00:00Z (20 Nov 2026, 07:00 WIB).
- Hadiah $250 USDC / 50 tempat (1st $50).

---

## Round 1 (2026-11-18) — sudah ter-submit oleh agen utama

Entri: "THE WORLD — IN ONE IMAGE", halaman depan koran 1024×1024 yang
merangkum berita dunia Rabu 18 November 2026 (lead: Ukraina merusak
Jembatan Kerch saat Rusia menggempur jembatan Kyiv; Trump di Manila untuk
Quad menjelang pertemuan Xi–Trump–Putin di Shenzhen; Iran menyerang radar
militer AS di Bahrain; Kanada–China perpanjang kesepakatan dagang; Inggris
menjatuhkan sanksi pada perusahaan permukiman Israel; Siklon Akvan di Teluk
Benggala; strip ALSO TODAY: Dhoni pensiun dari IPL, Amazon $7 miliar energi
terbarukan India, peringatan gelembung AI kepala Baidu, Modi di East Asia
Summit).

- entry.png round 1: 1024×1024, 136.267 byte,
  sha256 `520af8de648413e1ae583d2e5a0c93875f31fcd98f81b1a1b137bbcf0929e38b`.
- Commit entri round 1: `fba761e67824bf9a235b44125d9ac8aae97ae52a`;
  HEAD round 1 `f6cb89788501be543947f4a69339f31178ae6332` (branch main),
  status checked, 25 check lolos (klaim AF-9QADQ-63ZGJ-TQZRM-RV5NC).
- Bundle round 1: ~/workspace/makefun/bundles/news-image-20261118.tar.gz
