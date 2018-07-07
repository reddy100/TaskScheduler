from TaskScheduler.TaskScheduler.Dependency import TimeBasedDependency, TaskBasedDependency

class Task(object):
    def __init__(self, taskId, listOfDependencies, description = 'Default Task'):
        self.taskId = taskId
        self.description = description
        self.listOfDependencies = listOfDependencies
        self.listOfTimeDependencies = []
        self.listOfTaskDependencies = []
        self.isComplete = False
        self.assignDependencies()

    #TODO try to call this during object creation so it doesnt need to be called seperately
    def assignDependencies(self):
        for dependency in self.listOfDependencies:
            if isinstance(dependency, TimeBasedDependency):
                self.listOfTimeDependencies.append(dependency)
            elif isinstance(dependency, TaskBasedDependency):
                self.listOfTaskDependencies.append(dependency)
        if self.listOfTimeDependencies:
            sorted(self.listOfTimeDependencies, key = lambda x:x.timeDependency)
            self.listOfDependencies=None

    def isReady(self, listOfCompletedTasks=[]):
        for dependency in self.listOfTimeDependencies + self.listOfTaskDependencies:
            if not dependency.isReady(listOfCompletedTasks):
                return False
        return True

    def processTask(self):
        print(self.description)

    #TODO call this method during obejct creation and store in variable to avoid calling multiple times
    def isPureTimeDependentTask(self):
        return self.listOfTimeDependencies and not self.listOfTaskDependencies

    # TODO call this method during obejct creation and store in variable to avoid calling multiple times
    def isPureTaskDependentTask(self):
        return self.listOfTaskDependencies and not self.listOfTimeDependencies