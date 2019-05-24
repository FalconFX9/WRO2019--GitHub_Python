from sensor_and_motor_startup import *
from battery_level_test import better_compensation
import socket

# file_s = open('sensor_data.txt', 'w+')
# file_st = open('steering_data.txt', 'w+')
# file_x = open('time_data.txt', 'w+')
log_to_files = True
DEFAULT_SPEED = 60
"""
print("Attente connexion avec client")
print("Attente connexion avec le client graphique", file=sys.stderr)
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # construire une socket (famille adresse type internet, protocole TCP)
connexion_principale.bind(('', 12800))       # se prépare à écouter (tous clients potentiels, sur le port 12800)
connexion_principale.listen(5)               # ecoute jusqu'à 5 clients avant validation
connexion_avec_client, infos_connexion = connexion_principale.accept()  # bloque le programme tant qu'il n'y a pas de demande client
                                             # renvoie le socket client, (IP client,port client)
print("Connexion OK")
print("Connexion avec le client graphique : ", infos_connexion, file=sys.stderr)
"""
# PID Values --These are subjective and need to be tuned to the robot and mat
# Kp must be augmented or decreased until the robot follows the line smoothly --Higher Kp = Stronger corrections
# Same with Ki, after Kp is done --- note, Ki is not used in this case (error accumulation)
# Kd to 1, and move up or done until smooth, after Kp and Ki
# This process can take a VERY long time to fine-tune
K_PROPORTIONAL = 0.2
K_INTEGRAL = 0
K_DERIVATIVE = 0.17


class OneSensorLineFollower:
    target = 35
    error = 0
    last_error = 0
    derivative = 0
    integral = 0
    start_time = time()

    def __init__(self, color_sensor):
        self.__color_sensor = color_sensor

    def follower(self, side_of_line=None, kp=K_PROPORTIONAL, speed=DEFAULT_SPEED+better_compensation(),
                 sensor_target=target, kd=K_DERIVATIVE):
        if side_of_line is None:
            side_of_line = self.SideOfLine.left
        else:
            side_of_line = self.SideOfLine.right
        self.target = sensor_target
        self.error = self.target - float(self.__color_sensor.reflected_light_intensity)
        self.integral = self.error + self.integral
        self.derivative = self.error - self.last_error
        motor_steering = ((self.error * kp) + (self.integral * K_INTEGRAL) + (self.derivative * kd)) * float(
            side_of_line)
        self.last_error = self.error
        steer_pair.on(motor_steering, -speed)
        """
        if log_to_files:  # tant que pas appuie sur bouton de la brique
            msg_a_envoyer = str(self.__color_sensor.reflected_light_intensity) + ","
            msg_a_envoyer = msg_a_envoyer.encode()  # transforme string en binaire pour l'emission
            connexion_avec_client.send(msg_a_envoyer)
            sleep(0.1)
        else:  # pas de temps en seconde
            connexion_avec_client.send(b"fin")
            connexion_avec_client.close()  # fin de la connexion au client graphique
            print("Fin de la tache de connexion", file=sys.stderr)
            sleep(1)
        """
        """
        if log_to_files:
            file_s.write(str(self.__color_sensor.reflected_light_intensity) + '\n')
            file_x.write(str(round((time() - self.start_time), 1)) + '\n')
            file_st.write(str(motor_steering) + '\n')
        else:
            file_st.close()
            file_x.close()
            file_s.close()
        """

    class SideOfLine:
        left = 1
        right = -1


def hisp_center_follower(side_of_line=None, speed=DEFAULT_SPEED, kp=0.15, kd=0.17):
    follow = OneSensorLineFollower(center_sensor)
    follow.follower(side_of_line=side_of_line, kp=kp, kd=kd, speed=speed)


def losp_center_follower(side_of_line=None, speed=20, kp=0.6):
    follow = OneSensorLineFollower(center_sensor)
    follow.follower(side_of_line=side_of_line, kp=kp, speed=speed)


def hisp_left_follower(side_of_line=None, speed=DEFAULT_SPEED, kp=0.15):
    follow = OneSensorLineFollower(left_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=50)


def losp_left_follower(side_of_line=None, speed=20):
    follow = OneSensorLineFollower(left_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=0.4, speed=speed, sensor_target=45)


def hisp_right_follower(side_of_line=None, speed=DEFAULT_SPEED, kp=0.15):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=40)


def losp_right_follower(side_of_line=None, speed=20, kp=0.25):
    follow = OneSensorLineFollower(right_side_sensor)
    follow.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=30)


def timed_follower(sensor, timemax, side_of_line=None, speed=DEFAULT_SPEED, kp=0.15, ttarget=35, kd=0.17):
    follower = OneSensorLineFollower(sensor)
    timemax = time() + timemax
    while time() < timemax:
        follower.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=ttarget, kd=kd)


def follow_to_line(following_sensor=center_sensor, line_sensor=center_sensor, speed=DEFAULT_SPEED, side_of_line=None,
                   kp=0.25):
    follow = OneSensorLineFollower(following_sensor)
    while line_sensor.reflected_light_intensity > 20:
        follow.follower(side_of_line=side_of_line, kp=kp, speed=speed, sensor_target=45)


def follow_for_xlines(num_lines, sensor, side_of_line=None, speed=DEFAULT_SPEED, kp=0.15, ttarget=35, kd=0.17, line_sensor=center_sensor):
    counter = 0
    follower = OneSensorLineFollower(sensor)
    while counter < num_lines:
        follower.follower(side_of_line, kp, speed, ttarget, kd)
        if line_sensor.reflected_light_intensity < 30:
            if counter < num_lines - 1:
                counter = counter + 1
                timed_follower(sensor, 0.3, side_of_line, speed, kp, ttarget, kd)
            else:
                counter = counter + 1


def go_for_time_and_next_line(sensor, line_sensor, speed, side_of_line=None, kp=0.25, time=2):
    timed_follower(sensor, time, side_of_line, speed, kp)
    steer_pair.off()
    follow_to_line(sensor, line_sensor, speed-30, side_of_line, kp)
    steer_pair.off()


def turn_right(sensor):
    steer_pair.on_for_rotations(100, 40, 0.55)
    while sensor.reflected_light_intensity > 30:
        steer_pair.on(100, 30)
    steer_pair.off()


def turn_left(sensor):
    steer_pair.on_for_rotations(-100, 40, 0.55)
    while sensor.reflected_light_intensity > 30:
        steer_pair.on(-100, 30)
    steer_pair.off()
