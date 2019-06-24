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

Nous utiliserons l'Arduino UNO WiFi REV2 pour connecter notre plante. De ce fait nous avons élaborer un programme permettant de lire les valeurs des différents paramètres lié au bien être de la plante: luminosité, humidité et température.
Les différents capteurs à notre disposition sont :
- DHT11 capteur de température et d'humidité ambiant
- SEN0193 capteur d'humidité du sol
- APDS-9301 capteur de luminosité

![2019-06-24_16h57_47](https://user-images.githubusercontent.com/43552846/60029368-4f8c3300-96a1-11e9-8510-7e81c5d2c1e5.png)


Les données seront envoyées en permanence sur le site API thinger.io afin de pouvoir contrôler à distance les besoins de la plante et maîtriser au mieux ses différents paramètres. 

Nous récupérons ensuite les données de thinger.io à l'aide de token pour l'intégrer à notre code python. L'application est constitué d'une interface utilisateur qui demande de se connecter à l'API thinger.io avec le pseudo et le mot de passe propre à thinger.io. L'utilisateur a ensuite le choix entre plusieurs appareils connectés qui sont au préalable connectés à la plante. On choisit ensuite dans la base de donnée le nom de la plante que l'utilisateur possède. Puis l'application va comparer les données de thinger.io et de la base de donnée et selon l'intervalle minimum et maximum du besoin de la plante, 
