# -*- coding: UTF-8 -*-
# from time import sleep
import time


class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "rav"
        self.condiments = []

    def __str__(self):
        msg = 'HotDog'
        if len(self.condiments) > 0:
            msg = msg + ' with '
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = '大于8'
        if self.cooked_level > 5:
            self.cooked_string = '大于5'
        if self.cooked_level > 3:
            self.cooked_string = "大于3"
        else:
            self.cooked_string = "以上都不是"

    def add_condiment(self, condiment):
        self.condiments.append(condiment)


class X(HotDog):
    def __init__(self):
        HotDog.__init__(self)


myDog = HotDog()
myDog.cook(4)
print myDog.cooked_level
time.sleep(4)
print myDog.cooked_string
print myDog.condiments
print myDog
myDog.add_condiment('rose')
myDog.add_condiment('benjamin')
print myDog
