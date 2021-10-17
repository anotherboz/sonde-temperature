# Sonde de température

## Les mesures

Au démarrage, puis toutes les 30 minutes le micro-controleur intérroge les sondes de températeurs. Toutes les sondes sont interrogées en même temps.

A chaque relevé, la température est sauvegardée en mémoire ainsi que les 480 dernières (10 jours de données). Si le module Wifi dispose d'une configuration en client, il se connecte à internet et envoie les températures au serveur. Sinon, les différentes mesures sont gardée en mémoire et consultable par WebService.

## Le wifi

Au démarrage le micro-controleur est en mode "serveur". Le module Wifi est actif pendant 10 minutes. Il se désactive automatiquement après 10 minutes. Pour le réactiver il faut appuyer sur le bouton.
Après un appuie sur le bouton, le module redémarre automatiquement en mode "serveur".

Quand il est en mode serveur le module répond aux webservices: 
 
  - GET /temperature
  - GET /config
  - POST /config

### GET /temperature

Ce webservice retourne les dernières températures sous forme de tableau

```
{
    "node":string,
    "value":number
}[]
```

### GET /config

Ce webservice récupère la configuration actuelle du module. Cette configuration peut être programmée par défaut dans le module ou être "vide".

Si elle est vide, le module n'essaie pas de se connecter à internet et envoyer les données au serveur.

Le webservice retourne :

```
    {
        "sid": string,
        "password": string,
        "server": string,
        "message": string,
    }
```

### POST /config

Ce webservice met à jour la configuration du module.


## La lumière

Au démarrage le module clignote 3 fois lentement. Quand le mode serveur est activé, la lumière reste allumée. Pendant l'acquisition des température la diode clignote une fois rapidement, puis la lumière clignote rapidement pendant l'envoie des données au serveur (au moins une fois).
