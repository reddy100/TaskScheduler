import unittest
from mock import patch
from datetime import time
from TaskScheduler.TaskScheduler.Dependency import TimeBasedDependency, TaskBasedDependency
from TaskScheduler.TaskScheduler.Task import Task

class TimeBasedDependencyTest(unittest.TestCase):
    def setUp(self):
        self.timeDependency = TimeBasedDependency(time(8,20))

    @patch('TaskScheduler.TaskScheduler.Dependency.TimeBasedDependency.getTimeNow')
    def test_isReady_True(self, mock_getTimeNow):
        mock_now = time(8, 21)
        mock_getTimeNow.return_value = mock_now
        self.assertTrue(self.timeDependency.isReady())

    @patch('TaskScheduler.TaskScheduler.Dependency.TimeBasedDependency.getTimeNow')
    def test_isReady_False(self, mock_getTimeNow):
        mock_now = time(8, 0)
        mock_getTimeNow.return_value = mock_now
        self.assertFalse(self.timeDependency.isReady())

class TaskBasedDependencyTest(unittest.TestCase):
    def setUp(self):
        timeDependency = TimeBasedDependency(time(8,20))
        self.task = Task(1, [timeDependency])
        self.taskDependency = TaskBasedDependency(self.task)

    def test_isReady_True(self):
        self.assertTrue(self.taskDependency.isReady([self.task]))

    def test_isReady_False(self):
        self.assertFalse(self.taskDependency.isReady())


def main():
    unittest.main()

if __name__ == '__main__':
    main()