# plante_connectee

## Algorithme lecture de fichier Plante Connectée
MONNOT Kévin, LY Steven
Document technique projet plante connectée

Nous sommes l’entreprise Connected Flowers et nous souhaitons créer un objet connecté qui permettra à toute personne n’ayant aucune connaissance en botanique de pouvoir s’occuper d’un jardin chez soi. Nous souhaitons également fournir une base de données composée d’environ 30 plantes de la région contenant les spécifications ci-dessous :
1.	Le Nom de la plante 
2.	Une Catégorisation de la plante 
3.	La Description 
4.	Une ou plusieurs Photos
5.	L’humidité optimale du sol
6.	La température atmosphérique optimale
7.	La luminosité optimale 
8.	La période de floraison
L’objet connecté permettra quant à lui de capter l’humidité du sol, la luminosité et la température atmosphérique grâce à des capteurs relié à des machines tels que Arduino et Raspberry PI. Sachant que ces données seront directement en lien avec notre base de données ce qui permettra par le biais d’une application client (qui sera créer par notre entreprise) de pouvoir savoir en temps réel si les conditions sont optimales ou au contraire si les conditions deviennent dangereuses pour la survie de la plante.
 

 ![capture2](https://user-images.githubusercontent.com/43552846/50822098-1d745800-1331-11e9-81a8-8dd278467528.PNG)
Ces algorithmes vont permettre de convertir les données pour que l’on puisse le comprendre et que les machines Arduino et Raspberry puissent travailler avec. Les deux premiers algorithmes permettent aux machines de pouvoir passer du binaire au décimal et vice versa tandis que le troisième algorithme permet de stocker dans la mémoire tampon les octets lorsque l’ordinateur est trop occupé pour faire la tâche qu’il doit effectuer.
