from TaskScheduler.TaskList import TaskList

class Scheduler(object):
    def __init__(self, listOfTasks):
        self.listOfTasks = listOfTasks

    def beginScheduling(self):
        taskList = TaskList(self.listOfTasks)
        taskList.assignTasks()
        firstTask = taskList.getFirstTask()
        if not firstTask:
            return
        nextTaskToBeProcessed = firstTask
        while nextTaskToBeProcessed and not self._tasksComplete(taskList):
            nextTaskToBeProcessed.processTask()
            taskList.listOfCompletedTasks.append(nextTaskToBeProcessed)
            nextTaskToBeProcessed = taskList.getNextTask(nextTaskToBeProcessed)



    def _tasksComplete(self,taskList):
        numberOfRemainingTasks = len(taskList.listOfPureTimeDependentTasks)+len(taskList.listOfPureTaskDependentTasks)+len(taskList.listOfMixedDependencyTasks)
        return numberOfRemainingTasks==0