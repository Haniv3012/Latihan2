import streamlit as st

st.title("Chatbot 17 Agustus Sekolah")

st.write("Selamat datang di Chatbot 17 Agustus! Silakan tanyakan apa saja tentang kegiatan 17 Agustus di sekolah.")

# Pengetahuan tentang kegiatan 17 Agustus
knowledge = {
    "lomba balap karung": "Lomba balap karung adalah lomba tradisional yang menggunakan karung sebagai alat untuk melompat menuju garis finish.",
    "lomba makan kerupuk": "Peserta berlomba memakan kerupuk yang digantung tanpa menggunakan tangan.",
    "lomba tarik tambang": "Lomba tarik tambang melibatkan dua tim yang saling menarik tali tambang hingga salah satu tim melewati garis batas.",
    "lomba panjat pinang": "Peserta memanjat batang pinang yang dilumuri oli untuk mengambil hadiah di puncak.",
    "upacara bendera": "Upacara bendera dilakukan untuk memperingati Hari Kemerdekaan Indonesia pada tanggal 17 Agustus.",
    "paskibra": "Pasukan Pengibar Bendera (Paskibra) bertugas mengibarkan bendera merah putih saat upacara.",
    "pidato kemerdekaan": "Pidato kemerdekaan biasanya disampaikan oleh kepala sekolah atau tamu undangan.",
    "lomba kelereng": "Peserta berlomba membawa kelereng di atas sendok menuju garis finish.",
    "lomba memasukkan paku ke botol": "Peserta berlomba memasukkan paku ke dalam botol dengan mata tertutup.",
    "lomba estafet air": "Tim berlomba memindahkan air menggunakan gelas plastik secara estafet.",
    "lomba balap bakiak": "Peserta berjalan bersama menggunakan bakiak panjang menuju garis finish.",
    "lomba bola voli": "Pertandingan bola voli antar kelas atau antar guru dan siswa.",
    "lomba futsal": "Pertandingan futsal antar kelas atau antar tim sekolah.",
    "lomba cerdas cermat": "Lomba pengetahuan umum dan sejarah kemerdekaan Indonesia.",
    "lomba fashion show merah putih": "Peserta menampilkan busana bertema merah putih.",
    "lomba menghias kelas": "Setiap kelas berlomba menghias ruangan dengan tema kemerdekaan.",
    "lomba puisi kemerdekaan": "Peserta membacakan puisi bertema kemerdekaan Indonesia.",
    "lomba menyanyi lagu nasional": "Peserta menyanyikan lagu-lagu nasional seperti Indonesia Raya dan Hari Merdeka.",
    "lomba menggambar kemerdekaan": "Peserta menggambar dengan tema kemerdekaan Indonesia.",
    "lomba mewarnai": "Lomba mewarnai untuk siswa SD dengan tema kemerdekaan.",
    "lomba tebak kata": "Peserta menebak kata-kata yang berhubungan dengan kemerdekaan.",
    "lomba drama kemerdekaan": "Peserta menampilkan drama bertema perjuangan kemerdekaan.",
    "lomba pantun kemerdekaan": "Peserta membuat dan membacakan pantun bertema kemerdekaan.",
    "lomba yel-yel": "Tim membuat yel-yel kreatif bertema kemerdekaan.",
    "lomba estafet bendera": "Tim berlomba memindahkan bendera secara estafet.",
    "lomba puzzle pahlawan": "Peserta menyusun puzzle gambar pahlawan nasional.",
    "lomba kuis sejarah": "Kuis tentang sejarah kemerdekaan Indonesia.",
    "lomba poster kemerdekaan": "Peserta membuat poster bertema kemerdekaan.",
    "lomba bola basket": "Pertandingan bola basket antar kelas.",
    "lomba senam bersama": "Senam bersama seluruh warga sekolah sebelum lomba dimulai.",
    "lomba tumpeng": "Lomba membuat dan menghias tumpeng kemerdekaan.",
    "lomba pidato bahasa Inggris": "Peserta berpidato tentang kemerdekaan dalam bahasa Inggris.",
    "lomba vlog kemerdekaan": "Peserta membuat vlog bertema kemerdekaan Indonesia.",
    "lomba video kreatif": "Peserta membuat video kreatif bertema perjuangan kemerdekaan.",
    "lomba baca berita": "Peserta berlomba membaca berita bertema kemerdekaan.",
    "lomba menulis esai": "Peserta menulis esai tentang makna kemerdekaan.",
    "lomba poster digital": "Peserta membuat poster digital bertema kemerdekaan.",
    "lomba fotografi": "Lomba fotografi dengan tema kemerdekaan Indonesia.",
    "lomba kreasi daur ulang": "Peserta membuat karya dari barang bekas bertema kemerdekaan.",
    "lomba quiz online": "Quiz online seputar kemerdekaan Indonesia.",
    "lomba membuat komik": "Peserta membuat komik bertema perjuangan kemerdekaan.",
    "lomba menulis surat untuk pahlawan": "Peserta menulis surat untuk pahlawan nasional.",
    "lomba poster lingkungan": "Poster bertema kemerdekaan dan lingkungan hidup.",
    "lomba mural": "Peserta membuat mural bertema kemerdekaan di dinding sekolah.",
    "lomba kreasi topi merah putih": "Peserta membuat topi kreatif bertema merah putih.",
    "lomba membuat origami bendera": "Peserta membuat origami berbentuk bendera merah putih.",
    "lomba membuat gantungan kunci": "Peserta membuat gantungan kunci bertema kemerdekaan.",
    "lomba membuat puisi digital": "Peserta membuat puisi digital bertema kemerdekaan.",
    "lomba poster anti bullying": "Poster bertema kemerdekaan dan anti bullying di sekolah.",
    "lomba poster kesehatan": "Poster bertema kemerdekaan dan kesehatan di sekolah."
}

user_question = st.text_input("Tanyakan tentang kegiatan 17 Agustus di sekolah:")

if user_question:
    found = False
    for key, value in knowledge.items():
        if key in user_question.lower():
            st.info(value)
            found = True
    if not found:
        st.warning("Maaf, informasi tidak ditemukan. Silakan coba kata kunci lain.")
