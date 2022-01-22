# HOW DID I


## Installer micropython sur la carte

Cabler le fil sur le module comme indiqué dans ESP8266-01_USB-Stick Eng.pdf.

Télécharger la dernière version [ici](https://micropython.org/download/esp8266/).

```bash
$ pip install esptool

$ esptool.py --port /dev/ttyUSB0 erase_flash

$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20210418-v1.15.bin
```

Verifier que le module fonctionne avec Thonny... connecter le module, essayer l'instruction :
```python
print('hello')
```

## Pour le module Wifi

Pour gérer la connexion du module, voir [ici](http://docs.micropython.org/en/v1.15/esp8266/tutorial/network_basics.html).


On peut tester la connexion :
```python
import urequests
r = urequests.get('https://script.google.com/macros/s/(token)/exec')
```


### Les requêtes HTTP

Le tuto à lire : [ici](https://techtutorialsx.com/2017/06/11/esp32-esp8266-micropython-http-get-requests/)


