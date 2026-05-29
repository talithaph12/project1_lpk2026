import streamlit as st

# =========================================
# CONFIG PAGE
# =========================================
st.set_page_config(
    page_title="🧪 Calculator Standardisasi Larutan",
    page_icon="🧪",
    layout="wide"
)

# =========================================
# DARK MODE CUSTOM CSS
# =========================================
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3, h4 {
    color: #FFFFFF;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

div[data-testid="stMetric"] {
    background-color: #161B22;
    border-radius: 15px;
    padding: 15px;
}

.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #03C988;
    color: white;
}

div[data-testid="stNumberInput"] {
    background-color: #161B22;
    border-radius: 10px;
    padding: 5px;
}

div[data-testid="stSelectbox"] {
    background-color: #161B22;
    border-radius: 10px;
    padding: 5px;
}

div[data-testid="stRadio"] {
    background-color: #161B22;
    border-radius: 10px;
    padding: 10px;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================
st.markdown(
    """
    <h1 style='text-align: center;'>
    🧪 Calculator Standardisasi Larutan
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; font-size:18px;'>
    Kalkulator untuk menghitung Normalitas/Molaritas
    beserta %RPD hasil standardisasi larutan.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================================
# DATABASE
# =========================================
database = {
    "Asam Oksalat": {
        "BM": 126.07,
        "valensi": 2
    },

    "Boraks": {
        "BM": 381.37,
        "valensi": 2
    },

    "Kalium Dikromat": {
        "BM": 294.18,
        "valensi": 6
    },

    "CaCO3": {
        "BM": 100.09,
        "valensi": 2
    }
}

# =========================================
# PILIH METODE
# =========================================
metode = st.selectbox(
    "🧪 Pilih Metode Standardisasi",
    [
        "Alkalimetri",
        "Asidimetri",
        "Permanganometri",
        "Iodometri",
        "Kompleksometri"
    ]
)

# =========================================
# AUTO DATA
# =========================================
if metode == "Alkalimetri":

    baku = "Asam Oksalat"
    titran = "NaOH"
    default_massa = 630

elif metode == "Asidimetri":

    baku = "Boraks"
    titran = "HCl"
    default_massa = 500

elif metode == "Permanganometri":

    baku = "Asam Oksalat"
    titran = "KMnO4"
    default_massa = 630

elif metode == "Iodometri":

    baku = "Kalium Dikromat"
    titran = "Tiosulfat"
    default_massa = 500

elif metode == "Kompleksometri":

    baku = "CaCO3"
    titran = "EDTA"
    default_massa = 100

BM = database[baku]["BM"]
valensi = database[baku]["valensi"]

# =========================================
# LAYOUT
# =========================================
col1, col2 = st.columns([1,1])

# =========================================
# INPUT
# =========================================
with col1:

    st.subheader("📥 Input Data")

    massa = st.number_input(
        "Massa standar baku",
        value=float(default_massa)
    )

    satuan = st.selectbox(
        "Satuan Massa",
        ["mg", "g"]
    )

    if satuan == "g":
        massa_mg = massa * 1000
    else:
        massa_mg = massa

    st.info(f"Hasil konversi massa = {massa_mg:.2f} mg")

    st.markdown("### ⚗️ Volume Titran")

    vol1 = st.number_input(
        f"Volume {titran} pertama (mL)",
        min_value=0.0
    )

    vol2 = st.number_input(
        f"Volume {titran} kedua (mL)",
        min_value=0.0
    )

    st.markdown("### 🧪 Pengenceran")

    pengenceran = st.radio(
        "Apakah menggunakan pengenceran?",
        ["Ya", "Tidak"]
    )

    if pengenceran == "Ya":

        volume_total = st.number_input(
            "Volume total pengenceran (mL)",
            value=100.0
        )

        volume_pipet = st.number_input(
            "Volume yang dipipet untuk titrasi (mL)",
            value=25.0
        )

        FP = volume_total / volume_pipet

    else:
        FP = 1

    st.success(f"Faktor Pengali (FP) = {FP:.2f}")

    st.markdown("### 🧬 Database Otomatis")

    BM_input = st.number_input(
        "BM",
        value=float(BM)
    )

    valensi_input = st.number_input(
        "Valensi",
        value=float(valensi)
    )

    if metode != "Kompleksometri":

        BE_input = BM_input / valensi_input

        st.info(f"BE = {BE_input:.4f} mg/mgrek")

    hitung = st.button("🔍 Hitung Sekarang")

# =========================================
# OUTPUT
# =========================================
with col2:

    st.subheader("📤 Output Perhitungan")

    if hitung:

        if vol1 == 0 or vol2 == 0:

            st.error("Volume titran tidak boleh 0")

        else:

            # =====================================
            # NON KOMPLEKSOMETRI
            # =====================================
            if metode != "Kompleksometri":

                N1 = massa_mg / (
                    FP * vol1 * BE_input
                )

                N2 = massa_mg / (
                    FP * vol2 * BE_input
                )

                N_rata = (N1 + N2) / 2

                RPD = abs(
                    (N1 - N2) / N_rata
                ) * 100

                st.metric(
                    "Normalitas 1",
                    f"{N1:.4f} N"
                )

                st.metric(
                    "Normalitas 2",
                    f"{N2:.4f} N"
                )

                st.metric(
                    "Rerata Normalitas",
                    f"{N_rata:.4f} N"
                )

                st.metric(
                    "%RPD",
                    f"{RPD:.2f}%"
                )

                st.markdown("## 📋 Kesimpulan")

                if RPD < 10:

                    st.success(
                        f"""
                        Hasil standardisasi menunjukkan
                        rerata konsentrasi sebesar
                        {N_rata:.4f} N dengan nilai
                        %RPD sebesar {RPD:.2f}%.
                        
                        Presisi pengujian dinyatakan baik
                        karena %RPD < 10%.
                        """
                    )

                else:

                    st.warning(
                        f"""
                        Hasil standardisasi menunjukkan
                        rerata konsentrasi sebesar
                        {N_rata:.4f} N dengan nilai
                        %RPD sebesar {RPD:.2f}%.
                        
                        Presisi pengujian dinyatakan
                        kurang baik karena %RPD > 10%.
                        """
                    )

            # =====================================
            # KOMPLEKSOMETRI
            # =====================================
            else:

                M1 = massa_mg / (
                    FP * vol1 * BM_input
                )

                M2 = massa_mg / (
                    FP * vol2 * BM_input
                )

                M_rata = (M1 + M2) / 2

                RPD = abs(
                    (M1 - M2) / M_rata
                ) * 100

                st.metric(
                    "Molaritas 1",
                    f"{M1:.4f} M"
                )

                st.metric(
                    "Molaritas 2",
                    f"{M2:.4f} M"
                )

                st.metric(
                    "Rerata Molaritas",
                    f"{M_rata:.4f} M"
                )

                st.metric(
                    "%RPD",
                    f"{RPD:.2f}%"
                )

                st.markdown("## 📋 Kesimpulan")

                if RPD < 10:

                    st.success(
                        f"""
                        Hasil standardisasi menunjukkan
                        rerata konsentrasi sebesar
                        {M_rata:.4f} M dengan nilai
                        %RPD sebesar {RPD:.2f}%.
                        
                        Presisi pengujian dinyatakan baik
                        karena %RPD < 10%.
                        """
                    )

                else:

                    st.warning(
                        f"""
                        Hasil standardisasi menunjukkan
                        rerata konsentrasi sebesar
                        {M_rata:.4f} M dengan nilai
                        %RPD sebesar {RPD:.2f}%.
                        
                        Presisi pengujian dinyatakan
                        kurang baik karena %RPD > 10%.
                        """
                    )

            # =====================================
            # TRANSPARANSI
            # =====================================
            st.divider()

            st.markdown("## 🧮 Transparansi Perhitungan")

            if metode != "Kompleksometri":

                st.latex(
                    r'''
                    BE = \frac{BM}{Valensi}
                    '''
                )

                st.write(
                    f"BE = {BM_input} / {valensi_input}"
                )

                st.write(
                    f"BE = {BE_input:.4f} mg/mgrek"
                )

                st.latex(
                    r'''
                    N =
                    \frac{
                    massa\ standar\ baku
                    }{
                    FP \times Volume \times BE
                    }
                    '''
                )

            else:

                st.latex(
                    r'''
                    M =
                    \frac{
                    massa\ standar\ baku
                    }{
                    FP \times Volume \times BM
                    }
                    '''
                )

            st.latex(
                r'''
                \%RPD =
                \left|
                \frac{
                X_1 - X_2
                }{
                X_{rerata}
                }
                \right|
                \times 100\%
                '''
            )
