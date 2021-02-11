from time import sleep
class TrafficLigth:
    __color = "red"
    def running(self):
        while True:
            print("Горит красный цвет светофора")
            sleep(7)
            print("Горит желтый цвет светофора")
            sleep(2)
            print("Горит зеленый цвет светофора")
            sleep(7)
            print("Горит желтый цвет светофора")
            sleep(2)
trafficlight = TrafficLigth()
trafficlight.running()