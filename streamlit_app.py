import streamlit as st
import math

st.title("📐 Kalkulator Bangun Ruang")

# Pilihan bangun ruang
bangun = st.selectbox(
    "Pilih bangun ruang",
    ["Kubus", "Balok", "Tabung", "Bola"]
)

st.write("### Masukkan data:")

# --- KUBUS ---
if bangun == "Kubus":
    s = st.number_input("Panjang sisi (s)", min_value=0.0, step=0.1)

    if st.button("Hitung"):
        volume = s ** 3
        luas = 6 * (s ** 2)

        st.success(f"Volume Kubus: **{volume}**")
        st.success(f"Luas Permukaan Kubus: **{luas}**")

# --- BALOK ---
elif bangun == "Balok":
    p = st.number_input("Panjang (p)", min_value=0.0, step=0.1)
    l = st.number_input("Lebar (l)", min_value=0.0, step=0.1)
    t = st.number_input("Tinggi (t)", min_value=0.0, step=0.1)

    if st.button("Hitung"):
        volume = p * l * t
        luas = 2 * (p*l + p*t + l*t)

        st.success(f"Volume Balok: **{volume}**")
        st.success(f"Luas Permukaan Balok: **{luas}**")

# --- TABUNG ---
elif bangun == "Tabung":
    r = st.number_input("Jari-jari (r)", min_value=0.0, step=0.1)
    t = st.number_input("Tinggi (t)", min_value=0.0, step=0.1)

    if st.button("Hitung"):
        volume = math.pi * r * r * t
        luas = 2 * math.pi * r * (r + t)

        st.success(f"Volume Tabung: **{volume:.2f}**")
        st.success(f"Luas Permukaan Tabung: **{luas:.2f}**")

# --- BOLA ---
elif bangun == "Bola":
    r = st.number_input("Jari-jari (r)", min_value=0.0, step=0.1)

    if st.button("Hitung"):
        volume = (4/3) * math.pi * (r ** 3)
        luas = 4 * math.pi * (r ** 2)

        st.success(f"Volume Bola: **{volume:.2f}**")
        st.success(f"Luas Permukaan Bola: **{luas:.2f}**")
