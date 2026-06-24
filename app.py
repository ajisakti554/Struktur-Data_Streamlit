import streamlit as st

# ============================================================
# 1. KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Mastering Tree Data Structures",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    h1, h2, h3 {
        color: #0f172a;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f1f5f9;
        border-radius: 8px 8px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #005088 !important;
        color: white !important;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background-color: white;
    }
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 12px 15px;
    }
    .case-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-left: 6px solid #005088;
        border-radius: 10px;
        padding: 14px 20px;
        margin-bottom: 12px;
    }
    .case-card b {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# 2. SIDEBAR NAVIGATION
# ============================================================
with st.sidebar:
    st.title("📂 Navigation")
    selection = st.selectbox(
        "Pilih Studi Kasus:",
        [
            "Home",
            "1. Struktur Organisasi",
            "2. Sistem Folder",
            "3. Menu Website",
            "4. Decision Tree",
            "5. Silsilah Keluarga",
            "6. Struktur KDKMP",
            
        ]
    )
    st.divider()
    st.info("💡 **Tips:** Gunakan tab '📊 Visual' untuk grafik, '📖 Konsep DSA' untuk teori, dan '💻 Code DOT' untuk source code Graphviz yang bisa di-download.")
    st.divider()
    st.caption("📘 Mata Kuliah: Struktur Data\n\n🏫 IKOPIN University")

# ============================================================
# 3. HOME PAGE
# ============================================================
if selection == "Home":
    st.title("🌳 Visualisasi Struktur Data Tree")
    st.subheader("Platform Edukasi Interaktif untuk Memahami Hierarki")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Pohon (*Tree*) adalah struktur data non-linear yang digunakan untuk merepresentasikan hubungan
        hierarkis antara elemen-elemennya. Berbeda dengan Array atau Linked List yang bersifat linear
        (searah), Tree bercabang dan memiliki tingkatan (*level*).
        """)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Root", "1", help="Node teratas, tidak memiliki parent")
        m2.metric("Edge", "n − 1", help="Jumlah sisi pada tree dengan n node")
        m3.metric("Leaf", "≥ 1", help="Node tanpa child")
        m4.metric("Depth", "Var", help="Level terjauh dari root")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1653/1653704.png", width=220)

    st.markdown("### 📚 Studi Kasus yang Tersedia")
    cases = [
        ("1", "🏢", "Struktur Organisasi", "Aliran instruksi dalam organisasi perusahaan."),
        ("2", "💻", "Sistem Folder Komputer", "Manajemen direktori dan file dalam media penyimpanan."),
        ("3", "🌐", "Menu Website Universitas", "Struktur navigasi menu dan submenu pada website."),
        ("4", "🤖", "Decision Tree Sederhana", "Logika pengambilan keputusan kelulusan mahasiswa."),
        ("5", "👨‍👩‍👧", "Silsilah Keluarga", "Hubungan keturunan dan leluhur dalam keluarga."),
        ("6", "🏛️", "Struktur KDKMP", "Representasi struktur organisasi KDKMP menggunakan Tree."),
    ]
    for num, icon, title, desc in cases:
        st.markdown(f"""
        <div class="case-card">
        <b>{icon} Studi Kasus {num}: {title}</b><br>
        <span style="color:#64748b;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# 4. STUDI KASUS 1 — STRUKTUR ORGANISASI
# ============================================================
elif selection == "1. Struktur Organisasi":
    st.title("🏢 Studi Kasus 1: Struktur Organisasi Perusahaan")
    st.caption("Representasikan struktur organisasi menggunakan Tree.")
    ceo = st.text_input("Nama CEO:", "Aji Sakti Saputra")

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    dot = f"""
    digraph G {{
        graph [rankdir=TB, bgcolor=transparent];
        node [shape=record, style="filled,rounded", fillcolor="#E3F2FD", color="#005088", fontname="Arial"];
        edge [color="#64748b", arrowhead=vee];

        CEO [label="{{ {ceo} | Root Node }}", fillcolor="#005088", fontcolor=white];
        CTO [label="{{ CTO | Internal Node }}"];
        CMO [label="{{ CMO | Internal Node }}"];
        DEV [label="{{ Developer | Leaf Node }}"];
        DS [label="{{ Data Scientist | Leaf Node }}"];
        MKT [label="{{ Marketing | Leaf Node }}"];

        CEO -> CTO; CEO -> CMO;
        CTO -> DEV; CTO -> DS;
        CMO -> MKT;
    }}
    """

    with tab1:
        st.graphviz_chart(dot)
    with tab2:
        st.markdown("""
        ### Analisis Hierarki
        - **Root (Akar):** Titik tertinggi tanpa parent — diwakili oleh **CEO**, sumber dari seluruh instruksi.
        - **Internal Node:** Memiliki parent sekaligus child, contohnya **CTO** dan **CMO**.
        - **Leaf (Daun):** Node tanpa child, yaitu staf operasional seperti **Developer**, **Data Scientist**, dan **Marketing**.
        - **Depth CEO:** 0 — **Depth Developer:** 2.
        - Tree ini bersifat **unidirectional** (top-down): instruksi mengalir dari root ke leaf, sedangkan laporan mengalir sebaliknya.
        """)
    with tab3:
        st.code(dot, language="dot")
        st.download_button("⬇️ Download Kode DOT", dot, file_name="struktur_organisasi.dot")

# ============================================================
# 5. STUDI KASUS 2 — SISTEM FOLDER
# ============================================================
elif selection == "2. Sistem Folder":
    st.title("💻 Studi Kasus 2: Sistem Folder Komputer")
    st.caption("Buat Tree yang menggambarkan struktur folder.")
    username = st.text_input("Nama User:", "Aji_Sakti")

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    dot = f"""
    digraph G {{
        graph [rankdir=LR, bgcolor=transparent];
        node [shape=folder, style=filled, fillcolor="#FEF3C7", color="#D97706", fontname="Courier"];

        C [label="C:/ (Root)", fillcolor="#D97706", fontcolor=white];
        Users [label="Users"];
        Windows [label="Windows"];
        UserFolder [label="{username}"];
        Docs [label="Documents"];
        Pic [label="foto.jpg", shape=note, fillcolor="#ECFDF5"];
        Tugas [label="tugas_dsa.pdf", shape=note, fillcolor="#ECFDF5"];

        C -> Users; C -> Windows;
        Users -> UserFolder;
        UserFolder -> Docs;
        Docs -> Pic;
        Docs -> Tugas;
    }}
    """

    with tab1:
        st.graphviz_chart(dot)
    with tab2:
        st.info(f"**Path Traversal:** Untuk mengakses `foto.jpg`, sistem harus melewati `C:/ → Users → {username} → Documents`. Jalur unik ini disebut **Edge Path**.")
        st.markdown("""
        - Setiap folder dapat memiliki banyak **subfolder** (child), namun hanya satu **folder induk** (parent) — ciri khas struktur Tree.
        - File seperti `foto.jpg` dan `tugas_dsa.pdf` adalah **leaf node** karena tidak memiliki child.
        - Sistem operasi menavigasi struktur ini menyerupai algoritma **Depth-First Search (DFS)** saat melakukan pencarian file di File Explorer.
        """)
    with tab3:
        st.code(dot, language="dot")
        st.download_button("⬇️ Download Kode DOT", dot, file_name="sistem_folder.dot")

# ============================================================
# 6. STUDI KASUS 3 — MENU WEBSITE UNIVERSITAS
# ============================================================
elif selection == "3. Menu Website":
    st.title("🌐 Studi Kasus 3: Menu Website Universitas")
    st.caption("Representasikan menu dan submenu.")
    univ = st.text_input("Nama Universitas:", "IKOPIN University")

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    dot = f"""
    digraph G {{
        graph [rankdir=TB, bgcolor=transparent];
        node [shape=box, style="filled,rounded", fillcolor="#EDE9FE", color="#6D28D9", fontname="Arial"];
        edge [color="#A78BFA", arrowhead=vee];

        Home [label="{univ}", fillcolor="#6D28D9", fontcolor=white];
        Tentang [label="Tentang Kami"];
        Akademik [label="Akademik"];
        PMB [label="Penerimaan\\nMahasiswa Baru"];
        Berita [label="Berita"];

        Sejarah [label="Sejarah", shape=note, fillcolor="#F5F3FF"];
        Visi [label="Visi & Misi", shape=note, fillcolor="#F5F3FF"];
        Prodi [label="Program Studi"];
        Kalender [label="Kalender Akademik", shape=note, fillcolor="#F5F3FF"];
        S1 [label="S1", shape=note, fillcolor="#F5F3FF"];
        S2 [label="S2", shape=note, fillcolor="#F5F3FF"];
        Jalur [label="Jalur Masuk", shape=note, fillcolor="#F5F3FF"];
        Biaya [label="Biaya Kuliah", shape=note, fillcolor="#F5F3FF"];
        Pengumuman [label="Pengumuman", shape=note, fillcolor="#F5F3FF"];
        Artikel [label="Artikel", shape=note, fillcolor="#F5F3FF"];

        Home -> Tentang; Home -> Akademik; Home -> PMB; Home -> Berita;
        Tentang -> Sejarah; Tentang -> Visi;
        Akademik -> Prodi; Akademik -> Kalender;
        Prodi -> S1; Prodi -> S2;
        PMB -> Jalur; PMB -> Biaya;
        Berita -> Pengumuman; Berita -> Artikel;
    }}
    """

    with tab1:
        st.graphviz_chart(dot)
    with tab2:
        st.markdown("""
        ### Analisis Hierarki Navigasi
        - **Root:** Halaman utama website (Home), titik akses awal bagi seluruh pengunjung.
        - **Sibling Nodes:** Menu sejajar seperti **Tentang Kami**, **Akademik**, **PMB**, dan **Berita** berada pada level yang sama.
        - **Subtree:** Cabang **Akademik → Program Studi → (S1, S2)** adalah subtree yang dapat dianggap sebagai tree independen.
        - **Multilevel Hierarchy:** Tree memungkinkan navigasi bertingkat (menu → submenu) tanpa duplikasi data, berbeda dari struktur flat/linear.
        - Konsep ini banyak diterapkan pada **dropdown menu** dan **breadcrumb navigation** di website modern.
        """)
    with tab3:
        st.code(dot, language="dot")
        st.download_button("⬇️ Download Kode DOT", dot, file_name="menu_website.dot")

# ============================================================
# 7. STUDI KASUS 4 — DECISION TREE
# ============================================================
elif selection == "4. Decision Tree":
    st.title("🤖 Studi Kasus 4: Decision Tree Sederhana")
    st.caption("Buat Tree keputusan kelulusan mahasiswa.")
    ipk = st.slider("IPK Mahasiswa:", 0.0, 4.0, 3.0, step=0.01)

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    hasil = "LULUS ✅" if ipk >= 3.0 else "TINJAU ULANG ⚠️"
    warna = "#22C55E" if ipk >= 3.0 else "#EF4444"

    dot = """
    digraph G {
        node [style=filled, fontname="Arial"];
        Q [label="Apakah IPK >= 3.0?", shape=diamond, fillcolor="#F1F5F9"];
        Lulus [label="LULUS", shape=box, fillcolor="#BBF7D0"];
        Gagal [label="TINJAU ULANG", shape=box, fillcolor="#FECACA"];

        Q -> Lulus [label=" Ya ", color="#22C55E", fontcolor="#22C55E"];
        Q -> Gagal [label=" Tidak ", color="#EF4444", fontcolor="#EF4444"];
    }
    """

    with tab1:
        st.graphviz_chart(dot)
        st.markdown(
            f"#### Hasil untuk IPK **{ipk:.2f}** → "
            f"<span style='color:{warna}; font-weight:700;'>{hasil}</span>",
            unsafe_allow_html=True
        )
    with tab2:
        st.success("""
        Decision Tree memecah data menjadi himpunan bagian yang lebih kecil berdasarkan kondisi (*rule*),
        sambil pada saat yang sama pohon keputusan terkait dikembangkan secara bertahap (rekursif).
        """)
        st.markdown("""
        - **Decision Node:** Direpresentasikan sebagai diamond, berisi pertanyaan/kondisi (mis. "IPK ≥ 3.0?").
        - **Branch/Edge:** Jalur "Ya" atau "Tidak" sebagai hasil evaluasi kondisi.
        - **Leaf Node:** Hasil akhir keputusan, yaitu **LULUS** atau **TINJAU ULANG**.
        - Pada algoritma machine learning seperti **CART** atau **C4.5**, kondisi terbaik dipilih berdasarkan metrik seperti **Gini Index** atau **Entropy / Information Gain**.
        """)
    with tab3:
        st.code(dot, language="dot")
        st.download_button("⬇️ Download Kode DOT", dot, file_name="decision_tree.dot")

# ============================================================
# 8. STUDI KASUS 5 — SILSILAH KELUARGA
# ============================================================
elif selection == "5. Silsilah Keluarga":
    st.title("👨‍👩‍👧 Studi Kasus 5: Silsilah Keluarga")
    st.caption("Representasikan hubungan keluarga menggunakan Tree.")
    nama = st.text_input("Nama Anda:", "Aji")

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    dot = f"""
    digraph G {{
        graph [rankdir=TB, bgcolor=transparent];
        node [shape=ellipse, style=filled, fillcolor="#FCE7F3", color="#DB2777", fontname="Arial"];
        edge [color="#F472B6", arrowhead=vee];

        Kakek [label="Kakek\\n(Leluhur)", fillcolor="#DB2777", fontcolor=white];
        Ayah [label="Ayah"];
        Paman [label="Paman"];
        Saya [label="{nama}", fillcolor="#DB2777", fontcolor=white];
        Kakak [label="Kakak"];
        Sepupu [label="Sepupu"];

        Kakek -> Ayah; Kakek -> Paman;
        Ayah -> Saya; Ayah -> Kakak;
        Paman -> Sepupu;
    }}
    """

    with tab1:
        st.graphviz_chart(dot)
    with tab2:
        st.markdown(f"""
        ### Analisis Hubungan Keluarga
        - **Root:** Leluhur tertua yang tercatat dalam silsilah — di sini diwakili oleh **Kakek**.
        - **Ancestor (Leluhur):** Semua node pada jalur antara root dan suatu node, misalnya **Kakek** dan **Ayah** adalah ancestor dari **{nama}**.
        - **Descendant (Keturunan):** Semua node pada subtree di bawah suatu node, misalnya **{nama}** dan **Kakak** adalah descendant dari **Ayah**.
        - **Sibling:** Node dengan parent yang sama, seperti **{nama}** dan **Kakak**, atau **Ayah** dan **Paman**.
        - Silsilah di atas disederhanakan sebagai tree satu-jalur. Pada kondisi nyata (melibatkan ayah *dan* ibu), silsilah keluarga lebih tepat dimodelkan sebagai **DAG (Directed Acyclic Graph)** karena satu anak memiliki dua parent.
        """)
    with tab3:
        st.code(dot, language="dot")
        st.download_button("⬇️ Download Kode DOT", dot, file_name="silsilah_keluarga.dot")

# ============================================================
# 9. STUDI KASUS 6 — STRUKTUR KDKMP
# ============================================================
elif selection == "6. Struktur KDKMP":
    st.title("🏛️ Studi Kasus 6: Struktur Organisasi KDKMP")
    st.caption("Representasikan struktur organisasi KDKMP menggunakan Tree.")

    ketua = st.text_input("Nama Ketua KDKMP:", "Aji Sakti")

    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])

    dot = f"""
    digraph G {{
        graph [rankdir=TB, bgcolor=transparent];
        node [shape=record, style="filled,rounded", fillcolor="#E0F2FE", color="#0369A1", fontname="Arial"];
        edge [color="#64748b", arrowhead=vee];

        Ketua [label="{{ {ketua} | Ketua KDKMP (Root Node) }}", fillcolor="#0369A1", fontcolor=white];

        Wakil [label="{{ Wakil Ketua | Internal Node }}"];
        Sekretaris [label="{{ Sekretaris | Internal Node }}"];
        Bendahara [label="{{ Bendahara | Internal Node }}"];
        Akademik [label="{{ Divisi Akademik | Internal Node }}"];
        Humas [label="{{ Divisi Humas | Internal Node }}"];

        StaffA1 [label="{{ Staff Akademik 1 | Leaf Node }}"];
        StaffA2 [label="{{ Staff Akademik 2 | Leaf Node }}"];
        StaffH1 [label="{{ Staff Humas 1 | Leaf Node }}"];
        StaffH2 [label="{{ Staff Humas 2 | Leaf Node }}"];

        Ketua -> Wakil;
        Ketua -> Sekretaris;
        Ketua -> Bendahara;
        Ketua -> Akademik;
        Ketua -> Humas;

        Akademik -> StaffA1;
        Akademik -> StaffA2;

        Humas -> StaffH1;
        Humas -> StaffH2;
    }}
    """

    with tab1:
        st.graphviz_chart(dot)

    with tab2:
        st.markdown("""
        ### Analisis Hierarki KDKMP
        - **Root (Akar):** Node tertinggi yaitu **Ketua KDKMP**, pusat koordinasi organisasi.
        - **Internal Node:** Node yang memiliki parent dan child, seperti **Divisi Akademik** dan **Divisi Humas**.
        - **Leaf Node:** Node tanpa child, yaitu staf operasional.
        - **Depth Root:** 0  
        - **Depth Staff:** 2  
        - Struktur ini menunjukkan alur koordinasi dari pimpinan ke divisi lalu ke staf.
        """)

    with tab3:
        st.code(dot, language="dot")
        st.download_button(
            "⬇️ Download Kode DOT",
            dot,
            file_name="struktur_kdkmp.dot"
        )

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("🌳 Aplikasi Pembelajaran Struktur Data Tree | Dikembangkan untuk tujuan edukasi — IKOPIN University.")
