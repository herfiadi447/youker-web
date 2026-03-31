Berikut adalah **Product Requirements Document (PRD)** yang terstruktur dan siap kamu gunakan untuk pengembangan:

---

# **📄 PRODUCT REQUIREMENTS DOCUMENT (PRD)**

## **Web App / Landing Page – Jasa Pembuatan Website & Web App (Flask-Based)**

---

## **1. Overview Produk**

### **1.1 Nama Produk**

Youker Web Solutions (sementara, bisa disesuaikan dengan brand kamu)

### **1.2 Deskripsi Singkat**

Platform web berupa **landing page + web app sederhana** untuk menawarkan jasa pembuatan website, mulai dari:

* Website portofolio pribadi/perusahaan
* Web app skala menengah hingga kompleks
* Web GIS (Geographic Information System)
* Web app dengan integrasi chatbot (AI-based)

Frontend menggunakan **HTML/CSS/JS**, backend menggunakan **Flask (Python)**.

---

## **2. Tujuan Produk**

### **2.1 Tujuan Utama**

* Mendapatkan lead (calon klien)
* Menampilkan portofolio dan kredibilitas
* Menjelaskan layanan secara jelas dan terstruktur
* Menyediakan jalur komunikasi langsung (chat / form)

### **2.2 Success Metrics**

* Conversion rate (visitor → inquiry)
* Jumlah form masuk / chat masuk
* Bounce rate landing page
* Waktu rata-rata user di halaman

---

## **3. Target User**

### **3.1 Segmen Pengguna**

* Individu (freelancer, mahasiswa, kreator)
* UMKM / bisnis lokal
* Perusahaan skala kecil–menengah
* Instansi akademik / penelitian (khusus GIS)

### **3.2 Pain Points**

* Tidak punya website profesional
* Tidak paham teknis pembuatan web
* Butuh solusi custom (GIS, chatbot)
* Budget terbatas tapi ingin scalable

---

## **4. Value Proposition**

* 🔹 Custom web sesuai kebutuhan (bukan template biasa)
* 🔹 Spesialisasi di **Web GIS & Data Visualization**
* 🔹 Integrasi AI chatbot (nilai tambah besar)
* 🔹 Backend Python (Flask) → fleksibel untuk pengembangan lanjutan
* 🔹 Bisa scale dari landing page → web app kompleks

---

## **5. Fitur Utama**

### **5.1 Landing Page Sections**

#### **a. Hero Section**

* Headline kuat (contoh: “Bangun Website Profesional & Web App Custom untuk Bisnismu”)
* CTA:

  * “Konsultasi Gratis”
  * “Lihat Portofolio”

#### **b. Services Section**

Menampilkan kategori layanan:

* Website Portofolio
* Company Profile
* Web App Custom
* Web GIS
* Web + AI Chatbot

#### **c. Portfolio Section**

* List project (card/grid)
* Detail project (opsional halaman khusus)

#### **d. Pricing Section**

* Paket harga (basic, standard, premium)
* Custom pricing untuk proyek kompleks

#### **e. About Section**

* Profil kamu (Reski / brand Youker)
* Skill: GIS, Python, Web Dev

#### **f. Testimonial (opsional)**

* Review klien (dummy bisa dulu)

#### **g. CTA Section**

* Ajakan closing:

  * “Mulai Proyek Sekarang”

#### **h. Contact Section**

* Form:

  * Nama
  * Email
  * Kebutuhan
* Integrasi:

  * WhatsApp
  * Email

---

### **5.2 Fitur Web App (Backend - Flask)**

#### **a. Contact Form Handling**

* POST request ke Flask
* Simpan ke:

  * SQLite / PostgreSQL (disarankan: PostgreSQL)

#### **b. Admin Panel (opsional v1.1)**

* Login sederhana
* Lihat daftar inquiry

#### **c. Chatbot Integration**

* Integrasi API:

  * OpenAI / lokal LLM (future)
* Use case:

  * Tanya layanan
  * Rekomendasi paket

#### **d. Portfolio Management (opsional)**

* Tambah/edit project dari backend

---

### **5.3 Fitur Khusus (USP)**

#### **Web GIS Demo**

* Embed peta (Leaflet / Folium)
* Layer:

  * Shapefile / GeoJSON
* Fitur:

  * Toggle layer
  * Popup data

#### **AI Chatbot**

* Floating chat widget
* Bisa jawab:

  * Harga
  * Layanan
  * Alur kerja

---

## **6. User Flow**

### **Flow 1: Visitor → Client**

1. User buka landing page
2. Scroll lihat layanan
3. Tertarik → klik CTA
4. Isi form / chat WA
5. Masuk ke database
6. Follow-up manual

---

### **Flow 2: Chatbot Interaction**

1. User klik chatbot
2. Tanya: “berapa harga web?”
3. Bot jawab + rekomendasi paket
4. Redirect ke CTA / form

---

## **7. Tech Stack**

### **Frontend**

* HTML5
* CSS3 (Tailwind / Bootstrap opsional)
* JavaScript

### **Backend**

* Python
* Flask

### **Database**

* SQLite (MVP)
* PostgreSQL + PostGIS (untuk GIS)

### **GIS**

* Leaflet.js
* GeoJSON
* PostGIS (advanced)

### **Deployment**

* Vercel (frontend statis)
* VPS (backend Flask)

  * contoh: Hostinger / DigitalOcean

---

## **8. Non-Functional Requirements**

* ⚡ Fast loading (<3 detik)
* 📱 Responsive (mobile-first)
* 🔐 Basic security:

  * CSRF protection
  * Form validation
* 🌐 SEO-friendly

---

## **9. Roadmap Pengembangan**

### **Phase 1 (MVP)**

* Landing page statis
* Form contact (Flask)
* WhatsApp integration

### **Phase 2**

* Portfolio dinamis
* Database PostgreSQL
* UI lebih profesional

### **Phase 3**

* Chatbot AI
* Admin dashboard
* Web GIS demo

---

## **10. Risiko & Mitigasi**

| Risiko              | Mitigasi                    |
| ------------------- | --------------------------- |
| Tidak ada traffic   | SEO + share ke sosial media |
| Chatbot mahal (API) | Gunakan limit / model lokal |
| Deployment ribet    | Pisah frontend & backend    |

---

## **11. Estimasi Kompleksitas**

* MVP: **Low–Medium**
* Dengan GIS: **Medium–High**
* Dengan AI chatbot: **High**

---



---

## **5.4.2 Price List Layanan**

### **📌 JASA PEMBUATAN WEBSITE PORTFOLIO**

Layanan pembuatan website profesional untuk personal maupun perusahaan dengan desain modern, responsif, dan siap online.

---

### **🟢 Paket Personal Portfolio**

**Target:**
Individu (mahasiswa, freelancer, kreator)

**Fitur:**

* 1 halaman (landing page)
* Desain modern & responsif
* Section: About, Skills, Project, Contact
* Integrasi WhatsApp / Email
* Deploy online (hosting setup)

**💰 Harga (setelah diskon 30%):**
Rp **1.050.000 – Rp 1.750.000**

**🛠 Maintenance (opsional):**
Rp **70.000 / bulan**

---

### **🟡 Paket Professional Portfolio**

**Target:**
Personal branding yang lebih serius

**Fitur:**

* 2–4 halaman (Home, About, Project, Blog/Contact)
* Animasi & interaktif UI
* SEO dasar
* Optimasi performa
* Integrasi form database (Flask backend)

**💰 Harga (setelah diskon 30%):**
Rp **2.100.000 – Rp 3.850.000**

**🛠 Maintenance:**
Rp **105.000 – Rp 210.000 / bulan**

---

### **🔵 Paket Company Profile**

**Target:**
Perusahaan / UMKM

**Fitur:**

* 4–6 halaman
* Profil perusahaan lengkap
* Layanan/produk
* Testimoni klien
* Form kontak + database
* SEO dasar
* Optimasi mobile & kecepatan

**💰 Harga (setelah diskon 30%):**
Rp **3.500.000 – Rp 7.000.000**

**🛠 Maintenance:**
Rp **210.000 – Rp 350.000 / bulan**

---

## **5.4.3 Add-On (Opsional)**

| Fitur Tambahan              | Harga Setelah Diskon      |
| --------------------------- | ------------------------- |
| Custom domain (.com/.id)    | Rp 105.000 – Rp 210.000   |
| Setup hosting & deployment  | Rp 210.000 – Rp 700.000   |
| Integrasi AI Chatbot        | Rp 700.000 – Rp 3.500.000 |
| Training penggunaan website | Rp 140.000 – Rp 350.000   |

---

## **5.4.4 Catatan Pricing**

* Biaya hosting/server: ± Rp 300.000/bulan (dibayar klien)
* Harga fleksibel tergantung:

  * Kompleksitas fitur
  * Integrasi tambahan (GIS, API, dll)
* Estimasi pengerjaan:

  * **3 – 10 hari kerja (MVP)**
* Diskon 30% bersifat:

  * **Promo awal (limited)** → bisa jadi strategi urgency di landing page

---

## **5.4.5 Positioning Harga (Strategic Insight)**

Dengan harga setelah diskon:

* Kamu masuk ke kategori **mid-low pricing**
* Tapi dengan value:

  * Flask backend
  * GIS capability
  * AI chatbot

👉 Ini bisa diposisikan sebagai:

> “Affordable Custom Web Solution dengan teknologi advanced”

---

## **5.4.6 Integrasi ke Landing Page (UI/UX Notes)**

Di bagian pricing nanti:

* Gunakan **card layout**
* Highlight:

  * “🔥 Promo -30%”
  * “Paling populer” di paket tengah
* Tambahkan CTA:

  * “Mulai Sekarang”
  * “Konsultasi Gratis”

---

