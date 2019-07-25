import luigi
import gokart
import logging

logger = logging.getLogger(__name__)

class TaskA(gokart.TaskOnKart):
    def output(self):
        return self.make_target("task_a.pkl")

    def run(self):
        import warnings
        warnings.warn("test raise warnings at TaskA.run()")

        logging.info("TaskA.run()")
        self.dump("TASKA")


class TaskB(gokart.TaskOnKart):
    def requires(self):
        return TaskA()

    def output(self):
        return self.make_target("task_b.pkl")

    def run(self):
        data = self.load()
        logging.info("TaskB.run()")
        self.dump("TASKB" + data)
