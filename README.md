# plante_connectee


## Comment mettre en place cette plante connectée par vous même

### Le matériel nécessaire

Il faut d'abord disposer du matériel suivant suivant:
 * Une carte Arduino UNO WiFi REV2
 * Un capteur DHT11 (pour la température et l'humidité ambiante)
 * Une résistance de 5000 Ohm pour le capteur DHT11
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
 
 Dans le code Arduino il faut remplacer cerataines informations par les votres (c'est également précisé dans le code)
```arduino
#define USERNAME "Akane" // par votre nom de compte thinger.io
#define DEVICE_ID "arduino1" // par le nom de votre carte que vous avez créée thinger.io
#define DEVICE_CREDENTIAL "testtt" // par le credential que vous avez du renseigner lors de la création de votre carte sur thinger.io

#define SSID "kevin" // par le nom de votre réseau
#define SSID_PASSWORD "12345678" // par le mot de passe de votre réseau
```
 
 ### Comment connecter les capteurs
 
 Le DHT 11
 ![Arduino-and-DHT11_bb-800x800](https://user-images.githubusercontent.com/26713811/60217542-3f28b380-986d-11e9-9d7e-498869fcb515.png)
 
 
 Le cateur de lumnisoté
![20190517_105048](https://user-images.githubusercontent.com/26713811/60217789-cd9d3500-986d-11e9-84a2-5630e3ed1b6b.jpg)
![20190517_105057](https://user-images.githubusercontent.com/26713811/60217791-cece6200-986d-11e9-8c9c-d1d9807b527f.jpg)
![20190517_105103](https://user-images.githubusercontent.com/26713811/60217795-cfff8f00-986d-11e9-9a05-d91bb96f8e69.jpg)

Le capteur d'humidité du sol
 
