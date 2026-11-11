import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

données['chiffre_affaires'] = données['qte'] * données['prix']

# Graphique de ventes par région

figure = px.pie(données, values='qte', names='region', title='Quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')



# Graphique de ventes par produit

figure_produit = px.pie(données, values='qte', names='produit', title='Quantité vendue par produit')

figure_produit.write_html('ventes-par-produits.html')

print('ventes-par-produits.html généré avec succès !')



# Graphique de chiffre d'affaires par produit


figure_ca_produit = px.pie(données, values='chiffre_affaires', names='produit', title="Chiffre d'affaires par produit")

figure_ca_produit.write_html('chiffre-affaires-par-produits.html')

print('chiffre-affaires-par-produits.html généré avec succès !')