# Projet-info-L3
Le projet consiste à prédire le succès d'un film grâce à l'IA. 

Notre problématique est : "Comment estimer la note moyenne qu'un film obtiendra à sa sortie en prenant en compte son genre, sa langue et sa date de sortie ?"

Le .gitignore à été généré à partir de ce site (https://tools.alexandrai.org/fr/tools/gitignore-generator) de sorte à ce que les données ne soient pas sur Git directement. 

Le fichier analyse_de_données utilise la bibliothèque pandas. On analyse le fichier csv pour ensuite savoir comment le trier, on à utilisé le guide (https://docs.kanaries.net/fr) comme exemple pour rédiger notre code. 

    - Dans ce code on supprime les colonnes que nous n'utilisons pas pour que ce soit plus clair à analyser. 
    
    - Ensuite on supprime les lignes comprenant un films ou une ou plusieurs cases sont vides pour ne pas perturber notre programme. Cela correspond au maximum à une trentaine de film sur plus de 8000 c'est pourquoi on se permet de les supprimer. 

On traite les données pour qu'elles soient lisibles par le random forest, on remplace le texte par des nombres.
    
    - La colonne date se transforme en deux colonnes mois et année.

    - La colonne genre avec une liste de genres dedans se transforme en 1 colonne pour chaque genre avec des 1 et 0 (1 si ça concerne de film, 0 si non). 



Utilisation de l'IA : Comprendre l'acheminement du programme et les étapes à suivre. 
Obtenir les fonctions à utiliser pour certaines étapes.