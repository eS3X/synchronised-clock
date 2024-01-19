import datetime


class StatusChecker(object):
    def __init__(self):
        self.previous = None

    def clock(self):
        while True:
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S %p")
            if time_str != self.previous:
                print(time_str)
                self.previous = time_str


checker = StatusChecker()
checker.clock()
