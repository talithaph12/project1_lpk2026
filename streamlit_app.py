import streamlit as st

st.set_page_config(page_title="ChemLab Standardisasi", layout="centered")

st.title("🧪 ChemLab Standardisasi")
st.write("Perhitungan Konsentrasi Larutan pada Berbagai Metode Titrasi")

# DATABASE Mr
mr_database = {
    "NaOH": 40.00,
    "HCl": 36.46,
    "Na2CO3": 106.00,
    "KIO3": 214.00,
    "KMnO4": 158.04,
    "Na2S2O3": 248.18,
    "NaCl": 58.44,
    "AgNO3": 169.87,
    "CaCO3": 100.09,
    "EDTA": 292.24,
    "Asam Oksalat": 126.07
}

# DATABASE INDIKATOR
indikator_data = {
    "Alkalimetri": "Fenolftalein (PP)",
    "Asidimetri": "Metil Jingga (MO)",
    "Permanganometri": "Tanpa indikator (KMnO4 indikator sendiri)",
    "Iodometri": "Amilum",
    "Argentometri": "Kalium Kromat",
    "Kompleksometri": "Eriochrome Black T"
}

menu = st.selectbox(
    "Pilih Metode Standardisasi",
    [
        "Alkalimetri",
        "Asidimetri",
        "Permanganometri",
        "Iodometri",
        "Argentometri",
        "Kompleksometri"
    ]
)

st.divider()

# =====================
# ALKALIMETRI
# =====================
if menu == "Alkalimetri":
    st.header("Standardisasi Alkalimetri")

    senyawa = st.selectbox("Pilih Standar Primer", ["Asam Oksalat"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa standar primer (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=2.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Alkalimetri"):
        faktor = 100/25
        ekuivalen = massa / be
        normalitas = (massa) / (faktor * volume)
        molaritas = normalitas / valensi

        st.write(f"Rata-rata volume = {volume:.2f} mL")
        st.write(f"Rumus normalitas = (BE × faktor) / volume")
        st.success(f"Normalitas NaOH = {normalitas:.4f} N")
        st.success(f"Molaritas NaOH = {molaritas:.4f} M")

# =====================
# ASIDIMETRI
# =====================
elif menu == "Asidimetri":
    st.header("Standardisasi Asidimetri")

    senyawa = st.selectbox("Pilih Standar Primer", ["Na2CO3"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa Na2CO3 (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=2.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Asidimetri"):
        faktor = 1000
        ekuivalen = massa / be
        normalitas = (ekuivalen * faktor) / volume
        molaritas = normalitas / valensi

        st.success(f"Normalitas HCl = {normalitas:.4f} N")
        st.success(f"Molaritas HCl = {molaritas:.4f} M")

# =====================
# PERMANGANOMETRI
# =====================
elif menu == "Permanganometri":
    st.header("Standardisasi Permanganometri")

    senyawa = st.selectbox("Pilih Standar Primer", ["Asam Oksalat"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa Asam Oksalat (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=2.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Permanganometri"):
        faktor = 1000
        ekuivalen = massa / be
        normalitas = (ekuivalen * faktor) / volume
        molaritas = normalitas / 5

        st.success(f"Normalitas KMnO4 = {normalitas:.4f} N")
        st.success(f"Molaritas KMnO4 = {molaritas:.4f} M")

# =====================
# IODOMETRI
# =====================
elif menu == "Iodometri":
    st.header("Standardisasi Iodometri")

    senyawa = st.selectbox("Pilih Standar Primer", ["KIO3"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa KIO3 (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=6.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Iodometri"):
        faktor = 1000
        ekuivalen = massa / be
        normalitas = (ekuivalen * faktor) / volume
        molaritas = normalitas / valensi

        st.success(f"Normalitas Na2S2O3 = {normalitas:.4f} N")
        st.success(f"Molaritas Na2S2O3 = {molaritas:.4f} M")

# =====================
# ARGENTOMETRI
# =====================
elif menu == "Argentometri":
    st.header("Standardisasi Argentometri")

    senyawa = st.selectbox("Pilih Standar Primer", ["NaCl"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa NaCl (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=1.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Argentometri"):
        faktor = 1000
        ekuivalen = massa / be
        normalitas = (ekuivalen * faktor) / volume
        molaritas = normalitas / valensi

        st.success(f"Normalitas AgNO3 = {normalitas:.4f} N")
        st.success(f"Molaritas AgNO3 = {molaritas:.4f} M")

# =====================
# KOMPLEKSOMETRI
# =====================
elif menu == "Kompleksometri":
    st.header("Standardisasi Kompleksometri")

    senyawa = st.selectbox("Pilih Standar Primer", ["CaCO3"])

    mr = mr_database[senyawa]

    massa = st.number_input("Massa CaCO3 (g)", min_value=0.0)
    volume1 = st.number_input("Volume titrasi 1 (mL)", min_value=0.0)
    volume2 = st.number_input("Volume titrasi 2 (mL)", min_value=0.0)

    volume = (volume1 + volume2) / 2
    valensi = st.number_input("Valensi", min_value=1.0, value=2.0)

    be = mr / valensi

    st.info(f"Mr = {mr}")
    st.info(f"BE = {be:.2f}")
    st.info(f"Indikator = {indikator_data[menu]}")

    if st.button("Hitung Kompleksometri"):
        faktor = 1000
        ekuivalen = massa / be
        normalitas = (ekuivalen * faktor) / volume
        molaritas = normalitas / valensi

        st.success(f"Normalitas EDTA = {normalitas:.4f} N")
        st.success(f"Molaritas EDTA = {molaritas:.4f} M")

st.divider()

st.caption("Dibuat menggunakan Python Streamlit")
