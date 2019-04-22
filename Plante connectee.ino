#include <Adafruit_Sensor.h>
#include "DHT.h"

// we are including 2 library to use thinger.io server
#include <WiFi.h>
#include <ThingerWifi.h>

// we are including 2 library to use the APDS sensor
#include "Wire.h"
#include <Sparkfun_APDS9301_Library.h>



#define _DEBUG_
#define _DISABLE_TLS_
#define THINGER_USE_STATIC_MEMORY
#define THINGER_STATIC_MEMORY_SIZE 512

/**
 *  @brief Firstly we need to create an account in the thinger.io website. Then
 *         to connect the arduino with thinger.io we created an id and a
 *         password for the device. We connected the device to the wifi so we
 *         insert the SSID and the password.
 **/

#define USERNAME "Akane"
#define DEVICE_ID "arduino1"
#define DEVICE_CREDENTIAL "testtt"

#define SSID "kevin"
#define SSID_PASSWORD "12345678"

ThingerWifi thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

APDS9301 apds;

#define INT_PIN 3 // We'll connect the INT pin from the APDS sensor 
// to the PIN 2.

#define DHTPIN 2
#define DHTTYPE DHT11

DHT  dht(DHTPIN, DHTTYPE);
int  redPin             = 8;
int  greenPin           = 7;
int  moisturePin        = A3;
int  moistureValue;
bool humidityTempState;
bool moistureState;

/**
 * @brief This function configure pin of the color of the led.
 *        It also configure the wifi and initialize the light
 *        sensor.
 **/

void setup()
{
  thing.add_wifi(SSID, SSID_PASSWORD); // configure wifi network
  
  delay(5);    // The CCS811 wants a brief delay after startup.
  Serial.begin(115200);
  Wire.begin();

  // APDS9301 sensor setup.
  apds.begin(0x39);  // We're assuming you haven't changed the I2C
  //  address from the default by soldering the
  //  jumper on the back of the board.
  apds.setLowThreshold(0); // Sets the low threshold to 0, effectively
  //  disabling the low side interrupt.
  apds.setHighThreshold(50); // Sets the high threshold to 500. This
  //  is an arbitrary number I pulled out of thin
  //  air for purposes of the example. When the CH0
  //  reading exceeds this level, an interrupt will
  //  be issued on the INT pin.
  apds.enableInterrupt(APDS9301::INT_ON); // Enable the interrupt.
  apds.clearIntFlag();

  // Interrupt setup
  pinMode(INT_PIN, INPUT_PULLUP); // This pin must be a pullup or have
  //  a pullup resistor on it as the interrupt is a
  Serial.println(apds.getLowThreshold());
  Serial.println(apds.getHighThreshold());

  // This is used to get the value of the APDS sensor on thinger.io dashboard
  thing["luxValue"] >> outputValue(apds.readCH0Level());
  
  pinMode(INT_PIN, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  dht.begin();
}

/**
 * @brief This function launch three different fonctions : humidityTempValues
 *        read the humidity and temperature of the sensor and also determine
 *        if the threshold is exceeded or not. moistureValueFc read if it's not
 *        dry and also determine if the threshold is exceeded or not. colorLed
 *        turn on the color of the ledaccording to the state of the sensors.
 *        It also send values of a light sensor to the thinger.io server.
 **/

void loop()
{
  humidityTempValues();
  moistureValueFc();
  colorLed();
  lightSensor();
}

/**
 * @brief This function is used to read the humidity and the temperature
 *        of the DHT11 Humidity and Temperature. When the humidity is less
 *        than 30 or the temperature is above 30 the humidityTempState is
 *        true.
 **/

void humidityTempValues()
{
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  if (h <= 30 && t >= 30)
  {
    humidityTempState = false; 
  }
  else
  {
    humidityTempState = true; 
  }
}

/**
 * @brief This function is used to read the humidity and the temperature
 *        of the DSEN0193 Moisture. The sensor was calibrated and when the 
 *        sensor was dry the data was 500 while when it was wet the data was 
 *        250. So 20% drought equals 450. When the data is above than 450 the 
 *        moistureState is true.
 **/

void moistureValueFc()
{
  moistureValue = analogRead(moisturePin);
  if (moistureValue >= 450)
  {
    moistureState = true;
  }
  else
  {
    moistureState = false;
  }
}

/**
 * @brief This function is used to turn on the color of the led according to
 *        humidityTempState and moistureState. If humidityTempState is true
 *        the led will turn on red, if moistureState is true the led will turn
 *        on yellow but the priority is to humidityTempState. Otherwise the color 
 *        is green.
 **/


void colorLed()
{
  if (humidityTempState == true) 
  {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    
  }
  else if (moistureState == true)
  {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, HIGH);
  }
  else
  {
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
  }
}

/**
 *  @brief We are Using thing.handle function to send and get information from
 *        thinger.io. Every seconds we are sending to thinger.io the sensor's
 *        value and printing it on the monitor too.
 **/

void lightSensor()
{
  thing.handle();
  apds.clearIntFlag();
  delay(1000);
  Serial.print("Luminous flux: ");
  Serial.println(apds.readCH0Level(), 6);
}