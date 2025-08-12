import streamlit as st
import folium
from folium import plugins
import geopandas as gpd

# Dicionário que relaciona países a título e autor de um livro
country_books = {
    "Brazil": {"title": "Grande Sertão: Veredas", "author": "João Guimarães Rosa"},
    "United States": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    "United Kingdom": {"title": "1984", "author": "George Orwell"},
    "France": {"title": "Les Misérables", "author": "Victor Hugo"},
    # Adicione mais países e dados conforme necessário
}

# Carrega o GeoDataFrame dos países
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Configuração do Streamlit
st.title("Mapa Interativo de Livros por País")
st.write("Clique em um país para ver um livro e seu autor.")

# Criação do mapa
m = folium.Map(location=[20, 0], zoom_start=2)

# Função para adicionar os países ao mapa
def add_countries_to_map():
    for _, row in world.iterrows():
        country_name = row['name']
        # Verifica se há dados do livro para o país
        if country_name in country_books:
            book_info = country_books[country_name]
            popup_content = f"<strong>{country_name}</strong><br>Título: {book_info['title']}<br>Autor: {book_info['author']}"
        else:
            popup_content = f"<strong>{country_name}</strong><br>Sem dados de livro."
        
        folium.GeoJson(
            row['geometry'],
            popup=popup_content,
            style_function=lambda x: {'fillColor': '#B0C4DE', 'color': 'black', 'weight': 1, 'fillOpacity': 0.6}
        ).add_to(m)

# Adiciona os países ao mapa
add_countries_to_map()

# Renderiza o mapa
folium_static(m)
