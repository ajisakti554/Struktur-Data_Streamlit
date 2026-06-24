import streamlit as st

# 1. KONFIGURASI HALAMAN
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
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR NAVIGATION
with st.sidebar:
    st.title("📂 Navigation")
    selection = st.selectbox(
        "Pilih Studi Kasus:",
        ["Home", "1. Struktur Organisasi", "2. Sistem Folder", "3. Menu Website", "4. Decision Tree", "5. Silsilah Keluarga"]
    )
    st.divider()
    st.info("💡 **Tips:** Gunakan tab 'Visual' untuk melihat grafik dan 'Konsep DSA' untuk materi teori.")

# 3. HOME PAGE
if selection == "Home":
    st.title("🌳 Visualisasi Struktur Data Tree")
    st.subheader("Platform Edukasi Interaktif untuk Memahami Hierarki")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Pohon (*Tree*) adalah struktur data non-linear yang digunakan untuk merepresentasikan hubungan hierarkis antara elemen-elemennya. 
        Berbeda dengan Array atau Linked List yang bersifat linear (searah), Tree bercabang dan memiliki tingkatan (level).
        
        ### Apa yang akan kamu pelajari?
        1. **Hierarki Korporat:** Aliran instruksi dalam organisasi.
        2. **Sistem File:** Manajemen data dalam media penyimpanan.
        3. **Navigasi Web:** Struktur informasi antarmuka.
        4. **Logika Keputusan:** Dasar algoritma AI dan klasifikasi.
        5. **Genealogi:** Hubungan keturunan dan leluhur.
        """)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1653/1653704.png", width=250)

# 4. CASE STUDIES LOGIC
elif selection == "1. Struktur Organisasi":
    st.title("🏢 Struktur Organisasi Perusahaan")
    ceo = st.text_input("Nama CEO:", "Aji Sakti Saputra")
    
    tab1, tab2, tab3 = st.tabs(["📊 Visual", "📖 Konsep DSA", "💻 Code DOT"])
    
    with tab1:
        dot = f"""
        digraph G {{
            graph [rankdir=TB, bgcolor=transparent];
            node [shape=record, style="filled,rounded", fillcolor="#E3F2FD", color="#005088", fontname="Arial"];
            edge [color="#64748b", arrowhead=vee];
            
            CEO [label="{{ {ceo} | Root Node }}", fillcolor="#005088", fontcolor=white];
            CTO [label="{{ CTO | Parent Node }}"];
            CMO [label="{{ CMO | Parent Node }}"];
            DEV [label="{{ Developer | Leaf Node }}"];
            DS [label="{{ Data Scientist | Leaf Node }}"];
            MKT [label="{{ Marketing | Leaf Node }}"];
            
            CEO -> CTO; CEO -> CMO;
            CTO -> DEV; CTO -> DS;
            CMO -> MKT;
        }}
        """
        st.graphviz_chart(dot)
    
    with tab2:
        st.markdown("""
        ### Analisis Hierarki
        - **Root (Akar):** Titik tertinggi (CEO). Semua instruksi berasal dari sini.
        - **Internal Nodes:** Manajer atau Direktur (CTO/CMO) yang memiliki bawahan.
        - **Leaves (Daun):** Staf yang tidak memiliki bawahan lagi.
        """)
    with tab3:
        st.code(dot)

elif selection == "2. Sistem Folder":
    st.title("💻 Sistem Folder Komputer")
    tab1, tab2 = st.tabs(["📊 Visual", "📖 Konsep DSA"])
    with tab1:
        dot = """
        digraph G {
            graph [rankdir=LR, bgcolor=transparent];
            node [shape=folder, style=filled, fillcolor="#FEF3C7", color="#D97706", fontname="Courier"];
            
            C [label="C:/ (Root)", fillcolor="#D97706", fontcolor=white];
            Users [label="Users"];
            Windows [label="Windows"];
            Aji [label="Aji_Sakti"];
            Docs [label="Documents"];
            Pic [label="foto.jpg", shape=note, fillcolor="#ECFDF5"];
            
            C -> Users; C -> Windows;
            Users -> Aji;
            Aji -> Docs;
            Docs -> Pic;
        }
        """
        st.graphviz_chart(dot)
    with tab2:
        st.info("**Path Traversal:** Untuk mengakses `foto.jpg`, sistem harus melewati `C -> Users -> Aji_Sakti -> Documents`. Jalur ini disebut *Edge Path*.")

elif selection == "4. Decision Tree":
    st.title("🤖 Decision Tree (Logika Kelulusan)")
    ipk = st.slider("IPK Mahasiswa:", 0.0, 4.0, 3.0)
    
    tab1, tab2 = st.tabs(["📊 Visual", "📖 Konsep DSA"])
    with tab1:
        status_color = "#BBF7D0" if ipk >= 3.0 else "#FECACA"
        dot = f"""
        digraph G {{
            node [style=filled, fontname="Arial"];
            Q [label="Apakah IPK >= 3.0?", shape=diamond, fillcolor="#F1F5F9"];
            Lulus [label="LULUS", shape=box, fillcolor="#BBF7D0"];
            Gagal [label="TINJAU ULANG", shape=box, fillcolor="#FECACA"];
            
            Q -> Lulus [label=" Ya ", color="#22C55E", fontcolor="#22C55E"];
            Q -> Gagal [label=" Tidak ", color="#EF4444", fontcolor="#EF4444"];
        }}
        """
        st.graphviz_chart(dot)
    with tab2:
        st.success("Decision Tree memecah data menjadi himpunan bagian yang lebih kecil sambil pada saat yang sama pohon keputusan terkait dikembangkan secara bertahap.")

# Footer
st.markdown("---")
st.caption("Aplikasi Pembelajaran Struktur Data Tree | Dikembangkan untuk tujuan edukasi.")

