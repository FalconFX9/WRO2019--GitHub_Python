# -*- coding: utf-8 -*-
# Ce programme permet de récupérer les informations envoyées par 
# le robot EV3 en utilisant les SOCKETS afin de tracer en temps réel
# des graphiques avec MATPLOTLIB
# ATTENTION : les fenetres graphiques doivent être hors de la console
# préférences / consoleIPython / Graphique / Automatique

import socket                    # ici le client doit se connecter avec l'EV3 (=serveur)
import matplotlib.pyplot as plt  # pour tracer des graphiques

port = 12800                     # doit être identique sur l'EV3 (=serveur)
IPlegoEV3 = '192.168.137.3'        # à modifier si besoin
# '192.168.0.3' sur reseau freebox
# '172.16.5.41' sur reseau WIFILEGO

# construire une connexion socket (famille adresse type internet, protocole TCP)
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# se connecter avec le serveur (adresse IP legoEV3, port d'écoute du serveur)
connexion_avec_serveur.connect((IPlegoEV3, port))
print("Connexion établie avec l'EV3 (= serveur) sur le port {}".format(port))

plt.clf()                                     # nettoyer les anciens points
plt.xlabel('x (mm)') 
plt.ylabel('y (mm)')
plt.title('Position du robot EV3')
plt.axis([-1000,1000,-1000,1000])


def return_realtime_sensor_data():
    msg_recu = connexion_avec_serveur.recv(1024)
    msg_recu_decode = msg_recu.decode()  # transforme le binaire en string
    pos = msg_recu_decode.split(',')  # supprime les ,
    pos = float(pos[0])  # liste de n string en 2 réel
    # temps de pause < période d'envoie des messages  # longueur du message <1024
    return pos

"""
msg_recu = connexion_avec_serveur.recv(1024)
while msg_recu != b"fin":                     # "fin" enoyé par EV3 
    return_realtime_sensor_data()
    msg_recu = connexion_avec_serveur.recv(1024)
"""

connexion_avec_serveur.close()                # fermeture de la connexion
print("Fin de connexion avec l'EV3")          # avertissement pour utilisateur
