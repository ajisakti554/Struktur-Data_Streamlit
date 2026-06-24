a
import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Visualisasi Struktur Data Tree",
    page_icon="🌳",
    layout="wide"
)

# Judul Utama Aplikasi
st.title("🌳 Aplikasi Pembelajaran Struktur Data: Tree")
st.write("Aplikasi ini mendemonstrasikan implementasi struktur data *Tree* dalam berbagai skenario dunia nyata.")
st.markdown("---")

# Navigasi Sidebar
st.sidebar.header("Pilih Studi Kasus")
st.sidebar.write("Gunakan menu di bawah untuk berpindah studi kasus:")
studi_kasus = st.sidebar.radio(
    "Daftar Studi Kasus:",
    [
        "Studi Kasus 1: Struktur Organisasi",
        "Studi Kasus 2: Sistem Folder Komputer",
        "Studi Kasus 3: Menu Website Universitas",
        "Studi Kasus 4: Decision Tree Sederhana",
        "Studi Kasus 5: Silsilah Keluarga"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tips:** Setiap pohon divisualisasikan menggunakan Graphviz bawaan Streamlit.")

# ==========================================
# STUDI KASUS 1: STRUKTUR ORGANISASI
# ==========================================
if studi_kasus == "Studi Kasus 1: Struktur Organisasi":
    st.header("🏢 Studi Kasus 1: Struktur Organisasi Perusahaan")
    st.write("Representasi hierarki jabatan dari level tertinggi (Root) hingga level staf (Leaf).")
    
    # Input Interaktif Sederhana
    st.subheader("Kustomisasi Jabatan Utama")
    ceo_name = st.text_input("Nama CEO / Direktur Utama:", "Aji Sakti Saputra")
    
    # Sintaks Graphviz (DOT Language)
    dot_code = f"""
    digraph G {{
        rankdir=TB;
        node [shape=box, style=filled, color="#E3F2FD", fontname="Arial"];
        
        CEO [label="{ceo_name}\\n(Chief Executive Officer)", color="#4CAF50", fontcolor="white"];
        VP1 [label="VP of Engineering"];
        VP2 [label="VP of Marketing"];
        
        MGR1 [label="Engineering Manager"];
        MGR2 [label="Product Manager"];
        MGR3 [label="Social Media Manager"];
        
        STF1 [label="Data Scientist"];
        STF2 [label="Backend Developer"];
        STF3 [label="Content Writer"];
        
        CEO -> VP1;
        CEO -> VP2;
        
        VP1 -> MGR1;
        VP1 -> MGR2;
        VP2 -> MGR3;
        
        MGR1 -> STF1;
        MGR1 -> STF2;
        MGR3 -> STF3;
    }}
    """
    st.graphviz_chart(dot_code)
    
    with st.expander("📝 Penjelasan Konsep Tree"):
        st.markdown("""
        - **Root (Akar):** CEO (Level paling atas, tidak punya parent).
        - **Parent:** VP of Engineering adalah *parent* dari Engineering & Product Manager.
        - **Child:** Data Scientist dan Backend Dev adalah *child* dari Engineering Manager.
        - **Leaf (Daun):** Data Scientist, Backend Developer, Product Manager, dan Content Writer (tidak memiliki child lagi).
        """)

# ==========================================
# STUDI KASUS 2: SISTEM FOLDER KOMPUTER
# ==========================================
elif studi_kasus == "Studi Kasus 2: Sistem Folder Komputer":
    st.header("💻 Studi Kasus 2: Sistem Folder Komputer")
    st.write("Menggambarkan struktur direktori penyimpanan file di dalam komputer.")
    
    # Interaktivitas: Memilih folder untuk dibuka/ditutup
    show_subfolders = st.checkbox("Tampilkan isi folder 'Project_Data_Science'", value=True)
    
    sub_project_nodes = ""
    if show_subfolders:
        sub_project_nodes = """
        Project -> dataset_clean.csv;
        Project -> model_cnn.h5;
        Project -> dashboard_analytics.py;
        """
    
    dot_code = f"""
    digraph G {{
        rankdir=LR; // Mengubah arah dari Kiri ke Kanan agar seperti file explorer
        node [shape=folder, style=filled, color="#FFF3E0", fontname="Courier"];
        
        Root [label="C: (Local Disk)", color="#FF9800", fontcolor="white"];
        Documents [label="Documents"];
        Downloads [label="Downloads"];
        Music [label="Music"];
        
        Project [label="Project_Data_Science", color="#FFE082"];
        Resume [label="CV_Aji.pdf", shape=note, color="#E0F7FA"];
        Song [label="song.mp3", shape=note, color="#E0F7FA"];
        
        Root -> Documents;
        Root -> Downloads;
        Root -> Music;
        
        Documents -> Project;
        Documents -> Resume;
        Music -> Song;
        
        {sub_project_nodes}
    }}
    """
    st.graphviz_chart(dot_code)
    
    with st.expander("📝 Penjelasan Konsep Tree"):
        st.markdown("""
        - **Hierarki File:** Sistem operasi komputer menggunakan konsep *N-ary Tree* (pohon di mana satu node bisa memiliki banyak anak).
        - **Arah visualisasi:** Berbeda dengan struktur organisasi, sistem folder lebih natural dibaca dari kiri ke kanan (*Left to Right*).
        """)

# ==========================================
# STUDI KASUS 3: MENU WEBSITE UNIVERSITAS
# ==========================================
elif studi_kasus == "Studi Kasus 3: Menu Website Universitas":
    st.header("🌐 Studi Kasus 3: Menu Website Universitas")
    st.write("Representasi struktur menu navigasi utama beserta sub-menunya pada website kampus.")
    
    dot_code = """
    digraph G {
        rankdir=TB;
        node [shape=plaintext, fontname="Arial"];
        
        Home [label="🏠 Home\\n(Main Menu)", fontcolor="#29B6F6", fontsize=16];
        Profil [label="📋 Tentang Kami"];
        Akademik [label="🎓 Akademik"];
        Fasilitas [label="🏢 Fasilitas"];
        
        VisiMisi [label="• Visi & Misi"];
        Sejarah [label="• Sejarah"];
        Prodi [label="• Program Studi"];
        Kalender [label="• Kalender Akademik"];
        Lab [label="• Laboratorium Komputer"];
        Perpus [label="• Perpustakaan"];
        
        Home -> Profil;
        Home -> Akademik;
        Home -> Fasilitas;
        
        Profil -> VisiMisi;
        Profil -> Sejarah;
        
        Akademik -> Prodi;
        Akademik -> Kalender;
        
        Fasilitas -> Lab;
        Fasilitas -> Perpus;
    }
    """
    st.graphviz_chart(dot_code)
    
    with st.expander("📝 Penjelasan Konsep Tree"):
        st.markdown("""
        - **Navigasi Web:** Menu drop-down pada website memanfaatkan konsep Tree untuk mengelompokkan informasi secara logis.
        - Ketika pengguna mengarahkan kursor ke parent menu (contoh: *Akademik*), sistem akan memunculkan *children* node-nya (*Program Studi*, *Kalender*).
        """)

# ==========================================
# STUDI KASUS 4: DECISION TREE SEDERHANA
# ==========================================
elif studi_kasus == "Studi Kasus 4: Decision Tree Sederhana":
    st.header("🤖 Studi Kasus 4: Decision Tree Sederhana (Kelulusan Mahasiswa)")
    st.write("Pohon Keputusan yang mengklasifikasikan status kelulusan mahasiswa berdasarkan kondisi tertentu.")
    
    # Input Interaktif untuk Simulasi Jalur Tree
    st.subheader("Simulasi Logika Decision Tree")
    ipk = st.slider("1. Berapa IPK Mahasiswa?", 0.0, 4.0, 3.2, step=0.1)
    skripsi = st.radio("2. Apakah progress Tugas Akhir / Skripsi lancar?", ["Ya", "Tidak"])
    
    # Menentukan hasil jalur evaluasi
    status_kelulusan = ""
    if ipk >= 3.0:
        if skripsi == "Ya":
            status_kelulusan = "Lulus Tepat Waktu (Cumlaude/Sangat Memuaskan)"
        else:
            status_kelulusan = "Potensi Terlambat (Kendala Skripsi)"
    else:
        status_kelulusan = "Potensi Terlambat (Butuh Perbaikan Nilai)"
        
    st.success(f"**Hasil Prediksi Berdasarkan Jalur Tree:** {status_kelulusan}")
    
    # Warnai node aktif berdasarkan input slider/radio
    color_ipk_node = "#81C784" if ipk >= 3.0 else "#E57373"
    
    dot_code = f"""
    digraph G {{
        rankdir=TB;
        node [shape=ellipse, style=filled, fontname="Arial"];
        
        Root [label="Apakah IPK >= 3.0?", color="{color_ipk_node}"];
        Skripsi [label="Skripsi Lancar?", color="#FFF176"];
        
        Lulus1 [label="Lulus Tepat Waktu! 🎓", shape=box, color="#81C784"];
        Lulus2 [label="Terlambat (Perbaiki TA) ⚠️", shape=box, color="#E57373"];
        Lulus3 [label="Terlambat (Perbaiki Nilai) ⚠️", shape=box, color="#E57373"];
        
        Root -> Skripsi [label=" Ya (IPK={ipk})"];
        Root -> Lulus3 [label=" Tidak (IPK={ipk})"];
        
        Skripsi -> Lulus1 [label=" Ya"];
        Skripsi -> Lulus2 [label=" Tidak"];
    }}
    """
    st.graphviz_chart(dot_code)

# ==========================================
# STUDI KASUS 5: SILSILAH KELUARGA
# ==========================================
elif studi_kasus == "Studi Kasus 5: Silsilah Keluarga":
    st.header("👨‍👩‍👧‍👦 Studi Kasus 5: Silsilah Keluarga (Family Tree)")
    st.write("Menggambarkan hubungan keturunan/silsilah dari generasi kakek-nenek hingga anak-cucu.")
    
    dot_code = """
    digraph G {
        rankdir=TB;
        node [shape=oval, style=filled, fontname="Arial"];
        
        Kakek [label="Kakek & Nenek", color="#D1C4E9"];
        
        Ayah [label="Ayah (Anak 1)", color="#BBDEFB"];
        Paman [label="Paman (Anak 2)", color="#BBDEFB"];
        Bibi [label="Bibi (Anak 3)", color="#F8BBD0"];
        
        Kakak [label="Kakak (Cucu 1)", color="#C8E6C9"];
        Saya [label="Saya (Cucu 2)", color="#A5D6A7", penwidth=3];
        Sepupu [label="Sepupu (Cucu 3)", color="#FFE0B2"];
        
        Kakek -> Ayah;
        Kakek -> Paman;
        Kakek -> Bibi;
        
        Ayah -> Kakak;
        Ayah -> Saya;
        Paman -> Sepupu;
    }
    """
    st.graphviz_chart(dot_code)
    
    with st.expander("📝 Penjelasan Konsep Tree"):
        st.markdown("""
        - **Sibling:** Ayah, Paman, dan Bibi adalah *sibling* (saudara kandung) karena memiliki *parent* yang sama (Kakek & Nenek).
        - **Ancestor:** Kakek & Nenek adalah *ancestor* (leluhur) dari node 'Saya'.
        """)