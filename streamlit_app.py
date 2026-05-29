import streamlit as st

st.set_page_config(
    page_title="Web Calculator Standardisasi Larutan",
    layout="wide"
)

st.title("🧪 Web Calculator Standardisasi Larutan")

# =========================
# DATABASE
# =========================
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

# =========================
# PILIH METODE
# =========================
metode = st.selectbox(
    "Pilih Metode Standardisasi",
    [
        "Alkalimetri",
        "Asidimetri",
        "Permanganometri",
        "Iodometri",
        "Kompleksometri"
    ]
)

# =========================
# DATA OTOMATIS
# =========================
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

BE = BM / valensi

# =========================
# 2 KOLOM
# =========================
col1, col2 = st.columns(2)

# =========================
# INPUT
# =========================
with col1:

    st.header("📥 Input Data")

    massa = st.number_input(
        "Massa standar baku",
        value=float(default_massa)
    )

    satuan = st.selectbox(
        "Satuan massa",
        ["mg", "g"]
    )

    if satuan == "g":
        massa_mg = massa * 1000
    else:
        massa_mg = massa

    st.write(f"Massa dalam mg = {massa_mg:.2f} mg")

    vol1 = st.number_input(
        f"Volume {titran} 1 (mL)",
        min_value=0.0
    )

    vol2 = st.number_input(
        f"Volume {titran} 2 (mL)",
        min_value=0.0
    )

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
            "Volume yang dipipet (mL)",
            value=25.0
        )

        FP = volume_total / volume_pipet

    else:
        FP = 1

    st.write(f"Faktor Pengali = {FP:.2f}")

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
        st.write(f"BE = {BE_input:.4f}")

    hitung = st.button("Hitung")

# =========================
# OUTPUT
# =========================
with col2:

    st.header("📤 Output")

    if hitung:

        if vol1 == 0 or vol2 == 0:
            st.error("Volume tidak boleh 0")

        else:

            if metode != "Kompleksometri":

                N1 = massa_mg / (FP * vol1 * BE_input)
                N2 = massa_mg / (FP * vol2 * BE_input)

                N_rata = (N1 + N2) / 2

                RPD = abs((N1 - N2) / N_rata) * 100

                st.subheader("Hasil")

                st.write(f"Normalitas 1 = {N1:.5f} N")
                st.write(f"Normalitas 2 = {N2:.5f} N")
                st.write(f"Rerata Normalitas = {N_rata:.5f} N")
                st.write(f"%RPD = {RPD:.2f}%")

                if RPD < 10:
                    st.success("Presisi baik (%RPD < 10%)")
                else:
                    st.warning("Presisi kurang baik (%RPD > 10%)")

                st.subheader("Transparansi Perhitungan")

                st.latex(r"BE = \frac{BM}{Valensi}")

                st.write(f"BE = {BM_input} / {valensi_input}")
                st.write(f"BE = {BE_input:.4f}")

                st.latex(r"N = \frac{massa}{FP \times Volume \times BE}")

                st.write(
                    f"N1 = {massa_mg:.2f} / "
                    f"({FP:.2f} × {vol1:.2f} × {BE_input:.4f})"
                )

                st.write(f"N1 = {N1:.5f} N")

                st.write(
                    f"N2 = {massa_mg:.2f} / "
                    f"({FP:.2f} × {vol2:.2f} × {BE_input:.4f})"
                )

                st.write(f"N2 = {N2:.5f} N")

                st.latex(
                    r"\%RPD = \left| \frac{X_1-X_2}{X_{rerata}} \right| \times 100\%"
                )

                st.write(f"%RPD = {RPD:.2f}%")

            else:

                M1 = massa_mg / (FP * vol1 * BM_input)
                M2 = massa_mg / (FP * vol2 * BM_input)

                M_rata = (M1 + M2) / 2

                RPD = abs((M1 - M2) / M_rata) * 100

                st.subheader("Hasil")

                st.write(f"Molaritas 1 = {M1:.5f} M")
                st.write(f"Molaritas 2 = {M2:.5f} M")
                st.write(f"Rerata Molaritas = {M_rata:.5f} M")
                st.write(f"%RPD = {RPD:.2f}%")

                if RPD < 10:
                    st.success("Presisi baik (%RPD < 10%)")
                else:
                    st.warning("Presisi kurang baik (%RPD > 10%)")

                st.subheader("Transparansi Perhitungan")

                st.latex(r"M = \frac{massa}{FP \times Volume \times BM}")

                st.write(
                    f"M1 = {massa_mg:.2f} / "
                    f"({FP:.2f} × {vol1:.2f} × {BM_input:.4f})"
                )

                st.write(f"M1 = {M1:.5f} M")

                st.write(
                    f"M2 = {massa_mg:.2f} / "
                    f"({FP:.2f} × {vol2:.2f} × {BM_input:.4f})"
                )

                st.write(f"M2 = {M2:.5f} M")

                st.latex(
                    r"\%RPD = \left| \frac{X_1-X_2}{X_{rerata}} \right| \times 100\%"
                )

                st.write(f"%RPD = {RPD:.2f}%")
