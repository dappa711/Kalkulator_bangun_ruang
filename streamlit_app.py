import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Bangun Ruang",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

def calculate_cube(side):
    """Menghitung volume dan luas permukaan kubus"""
    volume = side ** 3
    surface_area = 6 * (side ** 2)
    return volume, surface_area

def calculate_cuboid(length, width, height):
    """Menghitung volume dan luas permukaan balok"""
    volume = length * width * height
    surface_area = 2 * (length*width + length*height + width*height)
    return volume, surface_area

def calculate_sphere(radius):
    """Menghitung volume dan luas permukaan bola"""
    volume = (4/3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)
    return volume, surface_area

def calculate_cylinder(radius, height):
    """Menghitung volume dan luas permukaan tabung"""
    volume = math.pi * (radius ** 2) * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area

def calculate_cone(radius, height):
    """Menghitung volume dan luas permukaan kerucut"""
    slant_height = math.sqrt(radius**2 + height**2)
    volume = (1/3) * math.pi * (radius ** 2) * height
    surface_area = math.pi * radius * (radius + slant_height)
    return volume, surface_area

def calculate_pyramid(base_length, base_width, height):
    """Menghitung volume dan luas permukaan limas segiempat"""
    volume = (1/3) * base_length * base_width * height
    slant_height1 = math.sqrt((base_length/2)**2 + height**2)
    slant_height2 = math.sqrt((base_width/2)**2 + height**2)
    surface_area = (base_length * base_width) + (base_length * slant_height2) + (base_width * slant_height1)
    return volume, surface_area

def calculate_triangular_prism(base, height_triangle, length):
    """Menghitung volume dan luas permukaan prisma segitiga"""
    volume = (1/2) * base * height_triangle * length
    surface_area = (base * height_triangle) + 3 * (length * base)
    return volume, surface_area

def plot_cube(side):
    """Membuat visualisasi 3D kubus"""
    fig = go.Figure()
    
    # Titik-titik kubus
    vertices = [
        [0, 0, 0], [side, 0, 0], [side, side, 0], [0, side, 0],
        [0, 0, side], [side, 0, side], [side, side, side], [0, side, side]
    ]
    
    # Sisi-sisi kubus
    edges = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom
        [4, 5], [5, 6], [6, 7], [7, 4],  # Top
        [0, 4], [1, 5], [2, 6], [3, 7]   # Vertical
    ]
    
    for edge in edges:
        x = [vertices[edge[0]][0], vertices[edge[1]][0]]
        y = [vertices[edge[0]][1], vertices[edge[1]][1]]
        z = [vertices[edge[0]][2], vertices[edge[1]][2]]
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue', width=5)))
    
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=400
    )
    return fig

def plot_sphere(radius):
    """Membuat visualisasi 3D bola"""
    phi = np.linspace(0, 2*np.pi, 30)
    theta = np.linspace(0, np.pi, 30)
    
    x = radius * np.outer(np.cos(phi), np.sin(theta))
    y = radius * np.outer(np.sin(phi), np.sin(theta))
    z = radius * np.outer(np.ones(np.size(phi)), np.cos(theta))
    
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Blues', opacity=0.8)])
    
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=400
    )
    return fig

def plot_cylinder(radius, height):
    """Membuat visualisasi 3D tabung"""
    z = np.linspace(0, height, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    
    fig = go.Figure(data=[go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale='Greens', opacity=0.8)])
    
    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=400
    )
    return fig

def main():
    st.title("📐 Kalkulator Bangun Ruang")
    st.markdown("""
    Aplikasi ini menghitung **volume** dan **luas permukaan** berbagai bangun ruang 3D.
    Pilih jenis bangun ruang dan masukkan parameter yang diperlukan.
    """)
    
    # Sidebar untuk pemilihan bangun ruang
    st.sidebar.header("Pilih Bangun Ruang")
    shape_options = {
        "Kubus": "cube",
        "Balok": "cuboid", 
        "Bola": "sphere",
        "Tabung": "cylinder",
        "Kerucut": "cone",
        "Limas Segiempat": "pyramid",
        "Prisma Segitiga": "triangular_prism"
    }
    
    selected_shape = st.sidebar.selectbox(
        "Jenis Bangun Ruang",
        list(shape_options.keys())
    )
    
    shape_type = shape_options[selected_shape]
    
    # Container untuk input parameter
    st.header(f"Parameter {selected_shape}")
    
    # Input parameter berdasarkan jenis bangun ruang
    if shape_type == "cube":
        col1, col2 = st.columns([2, 1])
        with col1:
            side = st.number_input("Panjang Sisi (cm)", min_value=0.1, value=5.0, step=0.1)
        
    elif shape_type == "cuboid":
        col1, col2, col3 = st.columns(3)
        with col1:
            length = st.number_input("Panjang (cm)", min_value=0.1, value=6.0, step=0.1)
        with col2:
            width = st.number_input("Lebar (cm)", min_value=0.1, value=4.0, step=0.1)
        with col3:
            height = st.number_input("Tinggi (cm)", min_value=0.1, value=3.0, step=0.1)
            
    elif shape_type == "sphere":
        col1, col2 = st.columns([2, 1])
        with col1:
            radius = st.number_input("Jari-jari (cm)", min_value=0.1, value=5.0, step=0.1)
            
    elif shape_type == "cylinder":
        col1, col2 = st.columns(2)
        with col1:
            radius = st.number_input("Jari-jari (cm)", min_value=0.1, value=3.0, step=0.1)
        with col2:
            height = st.number_input("Tinggi (cm)", min_value=0.1, value=8.0, step=0.1)
            
    elif shape_type == "cone":
        col1, col2 = st.columns(2)
        with col1:
            radius = st.number_input("Jari-jari (cm)", min_value=0.1, value=4.0, step=0.1)
        with col2:
            height = st.number_input("Tinggi (cm)", min_value=0.1, value=6.0, step=0.1)
            
    elif shape_type == "pyramid":
        col1, col2, col3 = st.columns(3)
        with col1:
            base_length = st.number_input("Panjang Alas (cm)", min_value=0.1, value=6.0, step=0.1)
        with col2:
            base_width = st.number_input("Lebar Alas (cm)", min_value=0.1, value=4.0, step=0.1)
        with col3:
            height = st.number_input("Tinggi Limas (cm)", min_value=0.1, value=5.0, step=0.1)
            
    elif shape_type == "triangular_prism":
        col1, col2, col3 = st.columns(3)
        with col1:
            base = st.number_input("Panjang Alas Segitiga (cm)", min_value=0.1, value=4.0, step=0.1)
        with col2:
            height_triangle = st.number_input("Tinggi Segitiga (cm)", min_value=0.1, value=3.0, step=0.1)
        with col3:
            length = st.number_input("Panjang Prisma (cm)", min_value=0.1, value=8.0, step=0.1)
    
    # Tombol hitung
    if st.button("🔄 Hitung Volume dan Luas Permukaan", type="primary"):
        
        # Perhitungan berdasarkan jenis bangun ruang
        if shape_type == "cube":
            volume, surface_area = calculate_cube(side)
            params = f"Sisi = {side} cm"
            
        elif shape_type == "cuboid":
            volume, surface_area = calculate_cuboid(length, width, height)
            params = f"Panjang = {length} cm, Lebar = {width} cm, Tinggi = {height} cm"
            
        elif shape_type == "sphere":
            volume, surface_area = calculate_sphere(radius)
            params = f"Jari-jari = {radius} cm"
            
        elif shape_type == "cylinder":
            volume, surface_area = calculate_cylinder(radius, height)
            params = f"Jari-jari = {radius} cm, Tinggi = {height} cm"
            
        elif shape_type == "cone":
            volume, surface_area = calculate_cone(radius, height)
            params = f"Jari-jari = {radius} cm, Tinggi = {height} cm"
            
        elif shape_type == "pyramid":
            volume, surface_area = calculate_pyramid(base_length, base_width, height)
            params = f"Panjang Alas = {base_length} cm, Lebar Alas = {base_width} cm, Tinggi = {height} cm"
            
        elif shape_type == "triangular_prism":
            volume, surface_area = calculate_triangular_prism(base, height_triangle, length)
            params = f"Alas Segitiga = {base} cm, Tinggi Segitiga = {height_triangle} cm, Panjang Prisma = {length} cm"
        
        # Tampilkan hasil
        st.success("✅ Perhitungan Selesai!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Hasil Perhitungan")
            st.metric("Volume", f"{volume:.2f} cm³")
            st.metric("Luas Permukaan", f"{surface_area:.2f} cm²")
            
            # Tampilkan parameter
            st.info(f"**Parameter:** {params}")
        
        with col2:
            st.subheader("🎯 Visualisasi 3D")
            
            # Buat visualisasi berdasarkan jenis bangun
            if shape_type == "cube":
                fig = plot_cube(side)
                st.plotly_chart(fig, use_container_width=True)
                
            elif shape_type == "sphere":
                fig = plot_sphere(radius)
                st.plotly_chart(fig, use_container_width=True)
                
            elif shape_type == "cylinder":
                fig = plot_cylinder(radius, height)
                st.plotly_chart(fig, use_container_width=True)
                
            else:
                st.info("Visualisasi 3D tersedia untuk Kubus, Bola, dan Tabung")
        
        # Tabel rumus
        st.subheader("📖 Rumus yang Digunakan")
        
        rumus_data = {
            "Kubus": {
                "Volume": "s³",
                "Luas Permukaan": "6 × s²"
            },
            "Balok": {
                "Volume": "p × l × t", 
                "Luas Permukaan": "2(pl + pt + lt)"
            },
            "Bola": {
                "Volume": "4/3 × π × r³",
                "Luas Permukaan": "4 × π × r²"
            },
            "Tabung": {
                "Volume": "π × r² × t",
                "Luas Permukaan": "2πr(r + t)"
            },
            "Kerucut": {
                "Volume": "1/3 × π × r² × t",
                "Luas Permukaan": "πr(r + s) dimana s = √(r² + t²)"
            },
            "Limas Segiempat": {
                "Volume": "1/3 × p × l × t",
                "Luas Permukaan": "pl + 2(½ × p × s1) + 2(½ × l × s2)"
            },
            "Prisma Segitiga": {
                "Volume": "½ × a × t_segitiga × t_prisma",
                "Luas Permukaan": "2 × (½ × a × t_segitiga) + (a + b + c) × t_prisma"
            }
        }
        
        df_rumus = pd.DataFrame(rumus_data).T
        st.dataframe(df_rumus, use_container_width=True)
        
        # Informasi tambahan
        with st.expander("💡 Tips dan Informasi"):
            st.markdown("""
            - **Volume** adalah besarnya ruang yang ditempati oleh bangun ruang
            - **Luas Permukaan** adalah total area semua permukaan bangun ruang
            - Gunakan satuan yang konsisten (semua dalam cm, m, dll.)
            - Untuk bangun tidak beraturan, gunakan metode displasemen air
            - π (pi) ≈ 3.14159
            """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**Kalkulator Bangun Ruang** • Dibuat dengan Streamlit • "
        "Gunakan untuk keperluan edukasi dan praktis"
    )

if __name__ == "__main__":
    main()
