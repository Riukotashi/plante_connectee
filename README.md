# plante_connectee


## Comment mettre en place cette plante connectée par vous même

### Le matériel nécessaire

Il faut d'abord disposer du matériel suivant suivant:
 * Une carte Arduino UNO WiFi REV2
 * Un capteur DHT11 (pour la température et l'humidité ambiante)
 * Un capteur SEN0193 (pour l'humidité du sol)
 * Un capteur APDS-9301 (capteur de lumière)
 * Un bus I2C pour le capteur de lumière
 
 ![2019-06-24_16h57_47](https://user-images.githubusercontent.com/43552846/60029368-4f8c3300-96a1-11e9-8510-7e81c5d2c1e5.png)
 
 
 ### Ce qu'il faut installer

Tout d'abord il est nécessaire d'installer plusieurs librairies pour le code arduino
Nous vous recommandons d'utiliser l'IDE web d'arduino pour compiler/téléverser le code
Voici la liste de toutes les librairies
* [thinger-io](https://github.com/thinger-io/Arduino-Library)
* [SparkFun APDS-9301](https://github.com/sparkfun/SparkFun_APDS9301_Library)
* [Adafruit Unified Sensor Library](https://github.com/adafruit/Adafruit_Sensor)
* [DHT 11](https://github.com/adafruit/DHT-sensor-library)
 
 
 ### Ce qu'il faut créer
 
 Un compte arduino pour utiliser l'ide web d'arduino
 Un compte thinger.io
 Une carte sur thinger .io
 
 
 ### Ce qu'il faut modifier
 
 Dans le code Arduino il faut remplacer cerataine information par les votre (c'est également préciser dans le code)
```arduino
#define USERNAME "Akane" // par votre nom de compte thinger.io
#define DEVICE_ID "arduino1" // par le nom de votre carte que vous avez créée thinger.io
#define DEVICE_CREDENTIAL "testtt" // par le credential que vous aves du renseigner lors de la création de votre carte sur thinger.io

#define SSID "kevin" // par le nom de votre réseau
#define SSID_PASSWORD "12345678" // par le mot de passe de votre réseau
```
 
 
 
 
 
Nous utiliserons l'Arduino UNO WiFi REV2 pour connecter notre plante. De ce fait nous avons élaborer un programme permettant de lire les valeurs des différents paramètres lié au bien être de la plante: luminosité, humidité et température.
Les différents capteurs à notre disposition sont :








Le code Arduino permet de lire les différentes données des capteurs. Il permet ainsi de lire le capteur de température DHT11 en °C, le capteur d'humidité du sol SEN0193 dont la valeur est exprimée par une constante allant de 250(mouillé) à 500(sec) et le capteur de luminosité APDS-9301 en lux.
Les données seront envoyées en permanence sur le site API thinger.io afin de pouvoir contrôler à distance les besoins de la plante et maîtriser au mieux ses différents paramètres. 

Nous récupérons ensuite les données de thinger.io à l'aide de token pour l'intégrer à notre code python. L'application est constitué d'une interface utilisateur qui demande de se connecter à l'API thinger.io avec le pseudo et le mot de passe propre à thinger.io. L'utilisateur a ensuite le choix entre plusieurs appareils connectés qui sont au préalable connectés à la plante. On choisit ensuite dans la base de donnée le nom de la plante que l'utilisateur possède. Puis l'application va comparer les données de thinger.io et de la base de donnée et selon l'intervalle minimum et maximum du besoin de la plante notre application conseillera l'utilisateur à arroser la plante ou non si l'humidité n'est pas assez élevé, éclairer ou non la plante selon l'intensité lumineuse ou bien baisser la température de la pièce si la plante demande une température idéal pour sa croissance. Ainsi l'utilisateur n'aura juste qu'à exécuter les commandes de l'application pour que sa plante sois la plus optimale possible selon des valeurs enregistrés et données par des experts botanistes. On optimisera ainsi un maximum le code python pour que l'application puisse se rafraichir toutes les 5 secondes afin que l'utilisateur puisse savoir par exemple quand arrêter d'arroser la plante.
