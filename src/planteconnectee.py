### We recommend you to see the documentation about thinger.io api to
### understand our code.
### The goals of our code is display to the user what he needs to do 
### to take care about his plant.
### First it authenticate a user to the thinger.io
### api to get his list of devices and ask him which device he want 
### to select, he has also to select a plant that is in our database.
### After we display to the user what he needs to do to take care about
### his plant.


import requests
import json
import getpass 
import time
from time import strftime
from datetime import datetime, date
from os import system

# Allow log and confidential informations when verbosity = 1.
verbosity = 1

url_thinger_api = "https://api.thinger.io/"

# parameter_get_token will be used to get the access token for thinger api
parameter_get_token ="oauth/token"
main_api_get_token = url_thinger_api + parameter_get_token


system('cls')   # clear the console (windows)
print ("Bienvenue sur l'interface plante connectée dédiée au bien être de votre plante. \n")



## The function authentification try to connect the user to thinger.io if the username
## and the password are right.
## It will return the username which will be use to get user device and also the
## reponse of thinger api with a json used to get the authorization token.
def authentification():
    security_count = 3 
    # security_count correspond to attempts for the user
    # to write wrong username and password
    while (security_count > 0):
        username = input("Veillez entrer votre nom d'utilisateur thinger.io : \n")
        password = getpass.getpass("Veillez entrer votre mot de passe : \n")
        security_count = security_count - 1

        # my_data is send to the thinger api, we are also sending the username
        # and the passord of the user
        mydata ={
        "Content--Type": "application/x-ww-form-urlencodes",
        "grant_type" : "password",
        "username": username,
        "password": password
                }

        # This is a post request is used to get an access token for thinger 
        # api, we need it to get an access to the date of thinger api
        thinger_api = requests.post(main_api_get_token, data=mydata)
        if (verbosity == 1):
            print ("LOG:", thinger_api.status_code)
        if (thinger_api.status_code == 200):
            # If username and password are correct, the thinger api return a
            #  success code (200) which means that the username and the 
            # passord are correct.
            return thinger_api, username
            # We return the correct username and what thinger api returned
        print("Mot de passe ou identifiant incorrect") 
        # Username or password is wrong so the user have to write again 
        # the good username and password
        print ("Tentatives restantes : ", security_count) 
        # Print the number of remaining attempts
        if (security_count == 0):    # After 3 wrong attempts the script stop
            print ("Arrêt de l'interface pour cause de sécurité !")
            exit()

## Here we are trying to catch some error which can append like a keyboard
## Interrupt or if we lost the connection with Thinger.io
try:
    thinger_api, username = authentification()
except KeyboardInterrupt:
    print ("Interruption du code détecté, fin de l'application.")
    exit()
except requests.exceptions.ConnectionError:
    print ("Contact perdu avec le serveur Thinger.IO Distant.")
    exit()

system('cls') # clear the console (windows)

# This is the access token from Thinger.io, it needs to be send at the end of
# end of the address which is used for the request with ?authorization=
json_access_token =  thinger_api.json()['access_token']
authorization = "?authorization=" + json_access_token

# This parameter will be used to get user devices
main_api_get_devices = url_thinger_api + "v1/users/" + username + "/devices" + authorization

print("Vous êtes bien connecté à thinger.io ! Nous allons prendre soin de votre plante ensemble en vous indiquant tous les besoins qu'elle a besoin.")

# This function ask the thinger.io api to get all the devices which are created
# and other information like if they are ON or OFF. We are printing the
# device's list which are ON to the user and the user can select one device.
# This function return the device seleted by the user
def get_device():
    # An input just to wait if the user want to load or reload the device's 
    # list
    input("Appuyer sur Entrée pour obtenir la liste des cartes allumées.\n")
    list_device = []

    # Here we are adding all the connected devices to a list
    for i in range (0, len(requests.get(main_api_get_devices).json())):
        if (requests.get(main_api_get_devices).json()[i]['connection']['active'] == True):
            list_device.append(requests.get(main_api_get_devices).json()[i]['device'])
    # Here we are printing all connected devices to the user if there is 
    # almost one device connected, if not we are returning the function
    if (len(list_device) > 0):
        print ("Voici la liste des cartes connectées :")
        # Printing all connected devices
        for i in range(0, len(list_device)):
            print (list_device[i])
        selected_device = input ("Selectionner la carte correspondante à la plante que vous voulez analyser :\n")
        for i in range(0, len(list_device)):
            if (selected_device == list_device[i]):
                return selected_device
        # If the user has seleted a wrong device we are returning the function
        # to restart the operation
        print ("La carte que vous avez sélectionné n'est pas disponible, veillez en sélectionner une nouvelle parmi la liste.")
        return get_device()
    print ("Veuilliez connecter une carte")
    return get_device()

## Here we are trying to catch some error which can append like a keyboard
## Interrupt or if we lost the connection with Thinger.io
try:
    selected_device = get_device()
except KeyboardInterrupt:
    print ("Interruption du code détecté, fin de l'application.")
    exit()
except requests.exceptions.ConnectionError:
    print ("Contact perdu avec le serveur Thinger.IO Distant.")
    exit()


# This parameter will be used to get device value
parameter_get_value = "v1/users/Akane/devices/" + selected_device + "/" 
main_api_get_value = url_thinger_api + parameter_get_value

# Those parameter will be used to get user devices
get_lux_value = main_api_get_value + "luxValue" + authorization
get_humidity_value = main_api_get_value + "humidityValue" + authorization
get_temperature_value = main_api_get_value + "temperatureValue" + authorization


system('cls') # Clear the console (windows)
print ("Vous avez selctionné une carte valide ")

## This function read a file, for each line the data will be add to a list
## when there is a ";" it will split the data and we will do that until
## the end of the file. This function also delete all the "\n".
## It is usefull to put csv file in a list.
## This function needs 1 paramater the path to the file that you want to
## be read and split.
##This function return a list of all the data which has been split

def read_file (path_to_file):
    tab = []
    file = open(path_to_file, 'r')
    for line in file:
        petit_tableau = []
        petit_tableau = line.replace('\n', '').split(';')
        tab.append(petit_tableau)
    file.close
    return tab

# Here we are reading a file which is kind of a data base of our plants
tab_plante = read_file("plante.csv")

## This function print the contents of all first index of a list it separe
## each content with "|" and when 3 content are printed we return to the
## next line.
## This function needs 1 parameter, a plant's list
def print_tab_plant (tab_plante):
    for i in range(1,len(tab_plante)):
        print (" ", tab_plante[i][0], "|", end='')
        if (i%3 == 0):
            print ("")
        i = i+2

# Printing the plant's list
print_tab_plant(tab_plante)


## This fucntion ask to the user which Plant he want to use if he select a
## plant that exist we return all the informtion about the plant in a list,
## if he choose an unvalid plant we ask him again.
## This function needs one parameter, a plant's list.
## This funtion return a list with only the information about the selected
## plant.
def select_plant (tab_plante):
    print("\ntaper le nom de la plante:")
    user_choice = input()
    j=1
    found = 0
    # Here we are searching if therse is a plant's name which correspond to
    # the user_choice
    while (j < len(tab_plante) and found == 0):
        if (tab_plante[j][0] == user_choice):
            found = 1
            selected_plant= tab_plante[j]
            
        j = j+1
    if (found == 1):
        system('cls')
        print ("Vous avez tapez un nom de plante valide")
        return selected_plant
    print ("Nom de plante invalide")
    return select_plant(tab_plante)

# Setting the plant selected by the user
try:
    selected_plant = select_plant(tab_plante)
except KeyboardInterrupt:
    print ("Interruption du code détecté, fin de l'application.")
    exit()

stop_reload = 0

## This loop print all the information that the user needs to take care about 
## his plant, it refresh the display every 5 second with the new data. It
## just compare the recommended data to the data from the sensors.
while (stop_reload == 0):
    state_sensors = []
    # sensor_not_good is here to count how many sensor has values that are too
    # high or to low 
    sensor_not_good = 0
    # We are testing that we get the temperature value from thinger.io
    if (requests.get(get_temperature_value).json() is None):
        state_sensors.append(("temperature", "Les informations du capteur de température sont indisponibles"))
    # If the temperature is too low we add to state_sensors that temperature
    # is too low
    elif (int(selected_plant[1]) < requests.get(get_temperature_value).json()):
        state_sensors.append(("temperature", 'La temprature est trop faible, il fait trop froid'))
        sensor_not_good = sensor_not_good + 1
    # If the temperature is too high we add to state_sensors that temperature
    # is high low
    elif (requests.get(get_temperature_value).json() < int(selected_plant[2])):
        state_sensors.append(("temperature", "La temprature est trop importante, il fait trop chaud"))
        sensor_not_good = sensor_not_good + 1
    # If the temperature is good we add to state_sensors that temperature
    # is good
    else:
        state_sensors.append(("temperature", "La temperature est optimale"))
    # We are testing that we get the humidity value from thinger.io
    if (requests.get(get_humidity_value).json() is None):
        state_sensors.append(("humidity", "Les informations du capteur d'humidité sont indisponibles"))
    # If the humidity is too low we add to state_sensors that humidity
    # is too low
    elif (requests.get(get_humidity_value).json() > int(selected_plant[3])):
        state_sensors.append(("humidity", "L'humidité du sol de la plante est insuffisante, il faut arroser votre plante"))
        sensor_not_good = sensor_not_good +1
    # If the humidity is good we add to state_sensors that humidity
    # is good
    else:
        state_sensors.append(("humidity", "L'humidité du sol de la plante est optimale"))

    # We are testing that we get the lux value from thinger.io
    if (requests.get(get_lux_value).json() is None):
        state_sensors.append(("lux", "Les informations du capteur d'humidité sont indisponibles"))
    # If the lux is too low we add to state_sensors that lux
    # is too low
    elif (requests.get(get_lux_value).json() < int(selected_plant[4])*75/100):
        state_sensors.append(("lux", "La luminosité de la plante est insuffisante, il faut mettre votre plante plus au soleil votre plante"))
        sensor_not_good = sensor_not_good +1
    # If the lux is too high we add to state_sensors that lux
    # is too high
    elif (requests.get(get_lux_value).json() > int(selected_plant[4])*150/100):
        state_sensors.append(("lux", "La luminosité de la plante est insuffisante, il faut mettre votre plante plus à l'ombre votre plante"))
        sensor_not_good = sensor_not_good +1
    # If the lux is good we add to state_sensors that lux
    # is good
    else:
        state_sensors.append(("lux", "La luminosité de la plante est optimale"))
    system('cls') # clear the console (windows)
    # We are printing the current date with the time
    print("Nous sommes le :", datetime.now().strftime("%d/%m/%Y"), "il est :", datetime.now().strftime("%H:%M:%S"))
    # If the state of one sensor or more isn't good we print to the user that
    # he needs to take care about his plant
    if sensor_not_good > 0:
        print("La santé de votre plante est en danger il faut vite prendre soin de votre plante!")
    # If the state of all sensors are good we print to the user that
    # he doesn't need to take care about his plant
    else:
        print("Votre plante va très bien :)")
    # Here we are printing all the state of the sensors
    for sensor, state in state_sensors:
        print (state)


    time.sleep(5)




