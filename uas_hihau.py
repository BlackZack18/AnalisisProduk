import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data CSV
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Fungsi fungsi
def Data_Mining(df_products, df_orders, df_order_items, df_products_name):
    st.write("Data Produk:")
    st.write(df_products.head())

    st.write("Data Order:")
    st.write(df_orders.head())

    st.write("Data Order Items:")
    st.write(df_order_items.head())

    st.write("Data Nama Produk:")
    st.write(df_products_name.head())

    # Pembersihan Data
    st.header("Pembersihan Data")
    st.subheader("Nilai yang Hilang")
    missing_values = df_orders.isnull().sum()
    st.write(missing_values)

    # Tampilkan data yang akan dihapus karena duplikasi
    st.write("Data yang Akan Dihapus karena Duplikasi:")
    duplicates_products = df_products[df_products.duplicated()]
    st.write(duplicates_products)

    st.write("Data Produk (Setelah Menghapus Duplikasi):")
    df_products.drop_duplicates(inplace=True)
    st.write(df_products.head())

    st.write("Data Order:")
    df_orders.drop_duplicates(inplace=True)
    st.write(df_orders.head())

    st.write("Data Order Items:")
    df_order_items.drop_duplicates(inplace=True)
    st.write(df_order_items.head())

    # Eksplorasi Data
    st.header("Eksplorasi Data")
    st.subheader("Distribusi Kategori Produk")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_products, x='product_category_name', ax=ax)
    ax.tick_params(axis='x', rotation=90)
    st.pyplot(fig)

    st.subheader("Korelasi Antar Variabel")
    numeric_columns = df_order_items.select_dtypes(include=['int', 'float']).columns
    corr = df_order_items[numeric_columns].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    st.pyplot(fig)
    with st.expander("Informasi korelasi antar variabel:"):
        st.write("- Nilai korelasi berkisar dari -1 hingga 1.")
        st.write("- Korelasi positif (nilai mendekati 1) menunjukkan hubungan positif antara variabel, artinya ketika satu variabel meningkat, variabel lainnya juga cenderung meningkat.")
        st.write("- Korelasi negatif (nilai mendekati -1) menunjukkan hubungan negatif antara variabel, artinya ketika satu variabel meningkat, variabel lainnya cenderung menurun.")
        st.write("- Korelasi mendekati 0 menunjukkan bahwa tidak ada hubungan linear antara variabel.")

    # Analisis Deskriptif
    st.header("Analisis Deskriptif")
    st.subheader("Statistik Deskriptif untuk Harga")
    st.write(df_order_items['price'].describe())
    with st.expander("Statistik Deskriptif :") :
        st.write("Untuk harga produk menunjukkan bahwa terdapat 112.650 entri dalam dataset. Rata-rata harga produk adalah sekitar USD.120,65 dengan standar deviasi sebesar USD.183,63, menunjukkan variasi yang signifikan dalam harga. Harga minimum produk adalah USD.0,85, sementara harga maksimumnya mencapai USD.6,735. Kuartil pertama (25 %) produk memiliki harga di bawah USD,39,9, sedangkan kuartil ketiga (75%) produk memiliki harga di bawah USD.134,9. Median harga produk, yang membagi dataset menjadi dua bagian yang sama besar, adalah USD.74,99.")

def Pertanyaan_Bisnis(df_products, df_products_name):
    # Pertanyaan 1
    st.write("## Pertanyaan 1 : Bagaimana distribusi tinggi produk? Berapa rata-rata nya?")

    # Tabel Tinggi Produk
    st.write("### Tabel Tinggi Produk")
    height_table = df_products[['product_category_name', 'product_height_cm']]
    height_table = height_table.rename(columns={'product_category_name': 'Nama Kategori Produk', 'product_height_cm': 'Tinggi Produk (cm)'})
    st.write(height_table)

    # Visualisasi Data
    st.write("### Distribusi Tinggi Produk")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df_products, x='product_height_cm', bins=20, kde=True, ax=ax, color='red')
    ax.set_title('Distribusi Tinggi Produk')
    ax.set_xlabel('Tinggi Produk (cm)')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)

    # Informasi Rata-rata, nilai max, dan nilai min Tinggi Produk
    average_height = df_products['product_height_cm'].mean()
    max_height = df_products['product_height_cm'].max()
    min_height = df_products['product_height_cm'].min()

    # Menampilkan informasi tambahan untuk tinggi produk
    with st.expander("Informasi Tinggi Produk"):
        st.write(f"Rata-rata Tinggi Produk: {average_height:.2f} cm")
        st.write(f"Tinggi Produk Tertinggi: {max_height} cm")
        st.write(f"Tinggi Produk Terendah: {min_height} cm")

    # Pertanyaan 2
    st.write("## Pertanyaan 2 : Berapa kisaran berat yang paling umum?")

    # Tabel Berat Produk
    st.write("### Tabel Berat Produk")
    weight_table = df_products[['product_category_name', 'product_weight_g']]
    weight_table = weight_table.rename(columns={'product_category_name': 'Nama Kategori Produk', 'product_weight_g': 'Berat Produk (g)'})
    st.write(weight_table)

    # Distribusi Berat Produk
    st.write("### Distribusi Berat Produk")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df_products, x='product_weight_g', bins=20, kde=True, ax=ax, color='orange')
    ax.set_title('Distribusi Berat Produk')
    ax.set_xlabel('Berat Produk (g)')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)
    
    # Informasi Rata-rata, nilai max, dan nilai min Berat Produk
    average_weight = df_products['product_weight_g'].mean()
    max_weight = df_products['product_weight_g'].max()
    min_weight = df_products['product_weight_g'].min()
    # Expander
    with st.expander("Informasi Berat Produk :") :
        st.write(f"Rata-rata Berat Produk: **{average_weight:.2f}** g")
        st.write(f"Berat Produk Tertinggi: **{max_weight}** g")
        st.write(f"Berat Produk Terendah: **{min_weight}** g")

    # Pertanyaan 3
    st.write("## Pertanyaan 3 : Berapa rata-rata panjang produk?")

    # Tabel Panjang Produk
    st.write("### Tabel Panjang Produk")
    length_table = df_products[['product_category_name', 'product_length_cm']]
    length_table = length_table.rename(columns={'product_category_name': 'Nama Kategori Produk', 'product_length_cm': 'Panjang Produk (cm)'})
    st.write(length_table)

    # Distribusi Panjang Produk
    st.write("### Distribusi Panjang Produk")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df_products, x='product_length_cm', bins=20, kde=True, ax=ax, color='salmon')
    ax.set_title('Distribusi Panjang Produk')
    ax.set_xlabel('Panjang Produk (cm)')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)

    # Informasi Rata-rata, nilai max, dan nilai min Panjang Produk
    average_length = df_products['product_length_cm'].mean()
    max_length = df_products['product_length_cm'].max()
    min_length = df_products['product_length_cm'].min()
    # Expander
    with st.expander("Informasi Panjang Produk :") :
        st.write(f"Rata-rata Panjang Produk: **{average_length:.2f}** cm")
        st.write(f"Panjang Produk Tertinggi: **{max_length}** cm")
        st.write(f"Panjang Produk Terendah: **{min_length}** cm")
    
    # Pertanyaan 4
    st.write("## Pertanyaan 4 : Berapakah lebar produk yang terbesar dan terkecil? Bagaimana distribusi nya?")

    # Tabel Lebar Produk
    st.write("### Tabel Lebar Produk")
    width_table = df_products[['product_category_name', 'product_width_cm']]
    width_table = width_table.rename(columns={'product_category_name': 'Nama Kategori Produk', 'product_width_cm': 'Lebar Produk (cm)'})
    st.write(width_table)

    # Distribusi Lebar Produk
    st.write("### Distribusi Lebar Produk")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df_products, x='product_width_cm', bins=20, kde=True, ax=ax, color='darkgrey')
    ax.set_title('Distribusi Lebar Produk')
    ax.set_xlabel('Lebar Produk (cm)')
    ax.set_ylabel('Frekuensi')
    st.pyplot(fig)

    # Informasi Rata-rata, nilai max, dan nilai min Lebar Produk
    max_width = df_products['product_width_cm'].max()
    min_width = df_products['product_width_cm'].min()
    # Expander
    with st.expander("Informasi Lebar Produk :") :
        st.write(f"Lebar Produk Tertinggi: **{max_width}** cm")
        st.write(f"Lebar Produk Terendah: **{min_width}** cm")

    # Pertanyaan 5
    st.write("## Pertanyaan 5 : Seberapa efektif pemilihan nama produk berdasarkan rata-rata panjang karakternya?")

    # Tabel Panjang Produk
    st.write("### Tabel Panjang Karakter Nama Produk")
    name_length_table = pd.merge(df_products[['product_category_name', 'product_name_lenght']], 
                                 df_products_name[['product_category_name', 'product_category_name_english']], 
                                 on='product_category_name')
    name_length_table = name_length_table.rename(columns={'product_category_name': 'Nama Kategori Produk', 
                                                          'product_category_name_english': 'Nama Produk', 
                                                          'product_name_lenght': 'Panjang Karakter Nama'})
    st.write(name_length_table)

    # Visualisasi distribusi
    st.write("### Distribusi Panjang Karakter Nama Produk")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.histplot(data=name_length_table, x='Panjang Karakter Nama', kde=True, ax=ax)
    plt.title('Distribusi Panjang Karakter Nama Produk berdasarkan Kategori', fontsize=16)
    plt.xlabel('Panjang Karakter Nama', fontsize=14)
    plt.ylabel('Frekuensi', fontsize=14)
    st.pyplot(fig)

    # Informasi Rata-rata, nilai max, dan nilai min Panjang Produk
    average_name_length = df_products['product_name_lenght'].mean()
    max_name_length = df_products['product_name_lenght'].max()
    min_name_length = df_products['product_name_lenght'].min()
    # Expander
    with st.expander("Evaluasi Efektifitas Nama Produk :") :
        st.write(f"Rata-rata Panjang Produk: **{average_name_length:.2f}** char")
        st.write(f"Panjang Produk Tertinggi: **{max_name_length}** char")
        st.write(f"Panjang Produk Terendah: **{min_name_length}** char")
        st.write("Berdasarkan data di atas, kita bisa mengetahui penggunaan jumlah karakter dari yang paling pendek hingga pailing panjang dalam penamaan prodak. Menurut data di atas,50 samapi 60 karakter adalah kisaran paling banyak dalam penamaan prodak,dari sini kita bisa pempertimbangkan jumlah karakter dalam penamaan prodak kita jika ingin memulai bisnis.")

# Load Dataset
df_products = load_data("https://raw.githubusercontent.com/BlackZack18/AnalisisProduk/main/products_dataset.csv")
df_orders = load_data("https://raw.githubusercontent.com/BlackZack18/AnalisisProduk/main/orders_dataset.csv")
df_order_items = load_data("https://raw.githubusercontent.com/BlackZack18/AnalisisProduk/main/order_items_dataset.csv")
df_products_name = load_data("https://raw.githubusercontent.com/BlackZack18/AnalisisProduk/main/product_category_name_translation.csv")


# Sidebar Menu
st.sidebar.write("# Menu :")
menu = st.sidebar.selectbox("",["Dashboard", "About Us"])

# Pilihan Dashboard
if menu == "Dashboard":
    # Header dan Tabs
    st.title("Dashboard Analisis Produk E-Commerce")

    tab1, tab2 = st.tabs(["Data Mining", "Pertanyaan Bisnis"])
    with tab1 :
        Data_Mining(df_products, df_orders, df_order_items, df_products_name)
    with tab2 :
        Pertanyaan_Bisnis(df_products, df_products_name)

# Pilihan About Us
elif menu == "About Us":
    st.title("Kelompok hihau")
    # Tampilkan anggota kelompok
    st.markdown(" **Anggota**:")
    st.markdown("  - 10122373 - Rakin Zakiy Saputra")
    st.markdown("  - 10122366 - Suswan Guevara Aryadhi")
    st.markdown("  - 10122363 - Arif Julianto")
    st.markdown("  - 10122383 - Mutiara Intan Suryani")
    st.markdown("  - 10122369 - Syahrial Usman Farahani")