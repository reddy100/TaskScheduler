import unittest
from mock import patch
from datetime import time
from TaskScheduler.TaskScheduler.Dependency import TimeBasedDependency, TaskBasedDependency
from TaskScheduler.TaskScheduler.Task import Task

class TaskTest(unittest.TestCase):
    def setUp(self):
        timeDependency = TimeBasedDependency(time(8,20))
        self.timeDependentTask = Task(1, [timeDependency])
        taskDependency = TaskBasedDependency(self.timeDependentTask)
        self.taskDependentTask = Task(2, [taskDependency])
        self.mixedDependencyTask = Task(3, [timeDependency, taskDependency])

    @patch('TaskScheduler.TaskScheduler.Dependency.TimeBasedDependency.getTimeNow')
    def test_isReady_timeDependentTask(self, mock_getTimeNow):
        mock_now = time(8, 21)
        mock_getTimeNow.return_value = mock_now
        self.assertTrue(self.timeDependentTask.isReady())

    def test_isReady_taskDependentTask(self):
        self.assertTrue(self.taskDependentTask.isReady([self.timeDependentTask]))

    @patch('TaskScheduler.TaskScheduler.Dependency.TimeBasedDependency.getTimeNow')
    def test_isReady_mixedDependencyTask(self, mock_getTimeNow):
        mock_now = time(8, 21)
        mock_getTimeNow.return_value = mock_now
        self.assertTrue(self.mixedDependencyTask.isReady([self.timeDependentTask]))

    def test_isPureTimeDependentTask(self):
        self.assertTrue(self.timeDependentTask.isPureTimeDependentTask())
        self.assertFalse(self.mixedDependencyTask.isPureTimeDependentTask())
        self.assertFalse(self.taskDependentTask.isPureTimeDependentTask())

    def test_isPureTaskDependentTask(self):
        self.assertTrue(self.taskDependentTask.isPureTaskDependentTask())
        self.assertFalse(self.mixedDependencyTask.isPureTaskDependentTask())
        self.assertFalse(self.timeDependentTask.isPureTaskDependentTask())


def main():
    unittest.main()

if __name__ == '__main__':
    main()
