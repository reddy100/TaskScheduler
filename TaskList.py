from datetime import datetime, time

class TaskList(object):
    def __init__(self, listOfTasks):
        self.listOfTasks = listOfTasks
        self.listOfPureTimeDependentTasks = []
        self.listOfPureTaskDependentTasks = []
        self.listOfMixedDependencyTasks = []
        self.listOfCompletedTasks = []
        self.taskDependencyGraph = {}

    # TODO try to call this during object creation so it doesnt need to be called seperately
    def assignTasks(self):
        for index in range(len(self.listOfTasks)):
            task = self.listOfTasks.pop(index)
            self.taskDependencyGraph[task] = task.listOfTaskDependencies
            if task.isPureTimeDependentTask():
                self.listOfPureTimeDependentTasks.append(task)
            elif task.isPureTaskDependentTask():
                self.listOfPureTaskDependentTasks.append(task)
            else:
                self.listOfMixedDependencyTasks.append(task)
        if self.listOfPureTimeDependentTasks:
            sorted(self.listOfPureTimeDependentTasks(), key=lambda x: x.listOfTimeDependencies[0])

    #TODO insert log statements instead of print
    #check if optimal to wait for first task here or in shceduler
    def getFirstTask(self):
        if self.listOfPureTimeDependentTasks:
            firstTask = self.listOfPureTimeDependentTasks.pop(0)
            if not firstTask.isReady(self.listOfCompletedTasks):
                self._waitTillReady()
            return firstTask
        else:
            print('Unable to find starting task for current list. Deadlocked')
            return

    def _waitTillReady(self, task):
        now = datetime.now()
        now_time = now.time()
        timeToWait = task.listOfTimeDependencies[0] - now_time
        time.sleep(timeToWait)


    def getNextTask(self):
        pass