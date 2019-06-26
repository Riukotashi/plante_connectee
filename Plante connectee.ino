/*
 * Plante_connectee
 *
 * Plante_connectee is a system that read the value of the Light sensor APDS-9301,
 * the Temperature sensor DHT11 and the Humidity sensor SEN0193.
 * In addition we are using thinger.io to connect our Arduino to a server
 * The data of these sensors is send to a dashboard.  
 * This will only work with an ARDUINO WIFI REV 2.
 */
 
 
#include <Adafruit_Sensor.h>
#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11


DHT  dht(DHTPIN, DHTTYPE);
int  humidityPin = A3;
int  moistureValue;


#define _DEBUG_
#define _DISABLE_TLS_
#define THINGER_USE_STATIC_MEMORY
#define THINGER_STATIC_MEMORY_SIZE 512

// we are including 2 library to use thinger.io server
#include <ThingerWifi.h>
#include <WiFi.h>


// we are including 2 library to use the APDS sensor
#include "Wire.h"
#include <Sparkfun_APDS9301_Library.h>

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

#define INT_PIN 2 // We'll connect the INT pin from the APDS sensor 
// to the PIN 2.

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
  
  dht.begin();

  pinMode(INT_PIN, OUTPUT);
  pinMode(5, OUTPUT);
 
  
  // This is used to get the value of the sensors on thinger.io dashboard
  thing["luxValue"] >> outputValue(apds.readCH0Level());
  thing["moistureValue"] >> outputValue(dht.readHumidity());
  thing["temperatureValue"] >> outputValue(dht.readTemperature());
  thing["humidityValue"] >> outputValue(humidityPin);
  
}

/**
 *  @brief We are Using thing.handle function to send and get information from
 *        thinger.io. Every seconds we are sending to thinger.io the sensors's
 *        value and printing it on the monitor too.
 **/

void loop() 
{
  thing.handle();
  apds.clearIntFlag();
  delay(1000);
}
