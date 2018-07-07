from TaskScheduler.TaskScheduler.TaskList import TaskList

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
        while nextTaskToBeProcessed and not self._allTasksComplete(taskList):
            nextTaskToBeProcessed.processTask()
            nextTaskToBeProcessed.isComplete = True
            taskList.listOfCompletedTasks.append(nextTaskToBeProcessed)
            nextTaskToBeProcessed = taskList.getNextTask(nextTaskToBeProcessed)



    def _allTasksComplete(self,taskList):
        return taskList.totalOpenTasks==0