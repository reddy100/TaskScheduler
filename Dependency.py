from datetime import datetime, time

class Dependency(object):
    pass


class TimeBasedDependency(Dependency):
    def __init__(self, timeDependency):
        self.timeDependency = timeDependency

    def isReady(self, listOfCompletedTasks):
        now = datetime.now()
        now_time = now.time()
        return now_time>=self.timeDependency


class TaskBasedDependency(Dependency):
    def __init__(self, taskDependency):
        self.taskDependency = taskDependency

    def isReady(self, listOfCompletedTasks):
        return self.taskDependency in listOfCompletedTasks