import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from supabase import create_client, Client
from groq import Groq

# Load environment variables (useful for local development, Vercel injects them automatically)
load_dotenv()

app = Flask(__name__)

# Initialize Supabase Client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = None
if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize Groq Client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = None
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)

# Email Settings (Owner's Email)
OWNER_EMAIL = "herfiadireskialviansyah03@gmail.com"
EMAIL_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_USER = os.getenv("SMTP_USER") # Usually your google email
EMAIL_PASS = os.getenv("SMTP_PASS") # Google App Password

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/gis")
def gis():
    return render_template("gis.html")

@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    service = data.get("service")
    message_text = data.get("message")

    if not all([name, email, service, message_text]):
        return jsonify({"success": False, "error": "Semua field harus diisi."}), 400

    # 1. Insert into Supabase Table "contacts"
    if supabase:
        try:
            supabase.table("contacts").insert({
                "name": name,
                "email": email,
                "service": service,
                "message": message_text
            }).execute()
        except Exception as e:
            print("Supabase Error:", e)
            # We continue even if DB fails to try sending email

    # 2. Send Email Notification
    if EMAIL_USER and EMAIL_PASS and EMAIL_PASS != "your_google_app_password":
        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_USER
            msg["To"] = OWNER_EMAIL
            msg["Subject"] = f"Proyek Baru: {service} dari {name}"

            body = f"""
            Ada permintaan proyek baru dari website:
            
            Nama: {name}
            Email: {email}
            Layanan: {service}
            Pesan:
            {message_text}
            """
            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Email Error:", e)
            # Jangan batalkan success jika email gagal tapi supabase berhasil
            pass

    return jsonify({"success": True, "message": "Pesan Anda telah berhasil dikirim!"})

@app.route("/api/chat", methods=["POST"])
def chat():
    if not groq_client:
        return jsonify({"success": False, "error": "Groq API key tidak diatur."}), 500
        
    data = request.json
    user_message = data.get("message", "")
    
    # Check if there's a language preference from frontend
    language = data.get("lang", "id") # default indonesian
    
    system_prompt = """
Anda adalah assistan virtual resmi untuk "Youker Web Solutions", sebuah agensi pengembangan web.
Layanan kami meliputi:
1. Website Portofolio (Personal / Profesional)
2. Company Profile
3. Web App Custom skala menengah hingga kompleks
4. Web GIS (Sistem Informasi Geografis) - Keahlian Utama
5. Integrasi Web + AI Chatbot

Informasi Tambahan:
- Pemilik: Reski
- Kontak WhatsApp (Reski): 082285580351
- Email: herfiadireskialviansyah03@gmail.com
- Kisaran Harga Portofolio: Rp 1.050.000 - Rp 3.850.000 (diskon 30% sedang berlaku)
- Kisaran Harga Company Profile: Rp 3.500.000 - Rp 7.000.000
- Custom Pricing tersedia untuk kebutuhan kompleks (GIS, AI, dll).

Berikan respons yang ringkas, ramah, profesional, dan gunakan poin-poin jika menjelaskan harga atau layanan.
Jika diminta kontak untuk proyek, berikan link WhatsApp (wa.me/6282285580351) atau sarankan untuk mengisi form di halaman ini.
"""

    if language == "en":
        system_prompt = """
You are the official virtual assistant for "Youker Web Solutions", a web development agency.
Our services include:
1. Portfolio Websites (Personal / Professional)
2. Company Profiles
3. Custom Web Apps (Mid to Complex scale)
4. Web GIS (Geographic Information Systems) - Core Expertise
5. Web + AI Chatbot Integrations

Additional Information:
- Owner: Reski
- WhatsApp Contact (Reski): +6282285580351
- Email: herfiadireskialviansyah03@gmail.com
- Portfolio Price Range: Rp 1,050,000 - Rp 3,850,000 (currently 30% off)
- Company Profile Price Range: Rp 3,500,000 - Rp 7,000,000
- Custom Pricing is available for complex needs (GIS, AI, etc.).

Provide concise, friendly, professional responses and use bullet points when explaining prices or services.
If asked for project contact, provide the WhatsApp link (wa.me/6282285580351) or suggest filling out the form on this page.
"""

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama3-8b-8192", 
            temperature=0.7,
            max_tokens=500,
        )
        
        reply = chat_completion.choices[0].message.content
        return jsonify({"success": True, "reply": reply})
    except Exception as e:
        print("Groq Error:", e)
        return jsonify({"success": False, "error": "Terjadi kesalahan pada AI Chatbot."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
