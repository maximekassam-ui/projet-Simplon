-- Vérification de l'import
SELECT * FROM ventes;


-- 3.a Chiffre d'affaires total
SELECT SUM(prix * qte) AS chiffre_affaires_total 
from ventes;
    -- Chiffre d'affaires total sur les 20j: 44 825 €
  
  
-- 3.b Ventes par produit
SELECT produit, SUM(qte) as total_ventes, SUM(prix * qte) as chiffre_affaires
from ventes 
group by produit
order by chiffre_affaires desc; 

	-- Produit A : 1750 exemplaires vendus pour 17 500 €
    -- Produit B : 1055 exemplaires vendus pour 15 825 €
    -- Produit C : 575 exemplaires vendus pour 11 500 €
    
   
-- 3.c Ventes par région
select region, SUM(qte) as total_ventes, SUM(prix * qte) as chiffre_affaires
from ventes 
group by region
order by chiffre_affaires desc; 

	-- Sud : 1775 exemplaires vendus pour 24 100 €
    -- Nord : 1605 exemplaires vendus pour 20 725 €