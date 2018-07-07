from datetime import datetime, time

class Dependency(object):
    pass


class TimeBasedDependency(Dependency):
    def __init__(self, timeDependency):
        self.timeDependency = timeDependency

    def getTimeNow(self):
        now = datetime.now()
        return now.time()

    def isReady(self, listOfCompletedTasks=[]):
        return self.getTimeNow() >=self.timeDependency


class TaskBasedDependency(Dependency):
    def __init__(self, taskDependency):
        self.taskDependency = taskDependency

    def isReady(self, listOfCompletedTasks=[]):
        return self.taskDependency in listOfCompletedTasks