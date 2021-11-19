import math

from Calls import Calls
from Call import Call
import copy
import Building


class Elevator:
    def __init__(self, elev):
        self.pos = 0
        self.stopTime = elev['_stopTime']
        self.startTime = elev['_startTime']
        self.openTime = elev['_openTime']
        self.closeTime = elev['_closeTime']
        self.maxFloor = elev['_maxFloor']
        self.minFloor = elev['_minFloor']
        self.speed = elev['_speed']
        self.id = elev['_id']

    def get_distance(self, src, dest):
        dif = abs(src - dest)
        dist = self.openTime + self.stopTime + self.closeTime + self.startTime + (dif / self.speed)
        return dist

    def __str__(self):
        return f"elev ID: {self.id}  start time: {self.startTime}  stop time: {self.stopTime}  open time: {self.openTime} +  close time: {self.closeTime}  max floor: {self.maxFloor}  min floor: {self.minFloor}  speed: {self.speed}  pos: {self.pos} "

    def get_speed(self):
        return self.speed

