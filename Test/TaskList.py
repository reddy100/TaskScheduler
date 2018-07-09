import unittest
from mock import patch
from datetime import time
from TaskScheduler.TaskScheduler.Dependency import TimeBasedDependency, TaskBasedDependency
from TaskScheduler.TaskScheduler.Task import Task
from TaskScheduler.TaskScheduler.TaskList import TaskList

class TaskTest(unittest.TestCase):
    def setUp(self):
        timeDependency = TimeBasedDependency(time(8,20))
        self.timeDependentTask = Task(1, [timeDependency])
        taskDependency = TaskBasedDependency(self.timeDependentTask)
        self.taskDependentTask = Task(2, [taskDependency])
        self.mixedDependencyTask = Task(3, [timeDependency, taskDependency])
        self.listOfTasks = [self.timeDependentTask, self.taskDependentTask, self.mixedDependencyTask]

    def test_assignTasks(self):
        taskList = TaskList(self.listOfTasks)
        self.assertEqual(len(taskList.listOfPureTimeDependentTasks), 0)
        self.assertEqual(len(taskList.listOfPureTaskDependentTasks), 0)
        self.assertEqual(len(taskList.listOfMixedDependencyTasks), 0)
        taskList.assignTasks()
        self.assertEqual(taskList.listOfPureTimeDependentTasks, [self.timeDependentTask])
        self.assertEqual(taskList.listOfPureTaskDependentTasks,[self.taskDependentTask])
        self.assertEqual(taskList.listOfMixedDependencyTasks , [self.mixedDependencyTask])

    def test_firstTask_None(self):
        taskList = TaskList(self.listOfTasks)
        self.assertIsNone(taskList.getFirstTask())

    @patch('TaskScheduler.TaskScheduler.Dependency.TimeBasedDependency.getTimeNow')
    def test_firstTask(self, mock_getTimeNow):
        taskList = TaskList(self.listOfTasks)
        taskList.assignTasks()
        mock_now = time(8, 21)
        mock_getTimeNow.return_value = mock_now
        self.assertEqual(taskList.getFirstTask(), self.timeDependentTask)


def main():
    unittest.main()

if __name__ == '__main__':
    main()