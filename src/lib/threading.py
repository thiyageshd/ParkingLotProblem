import datetime
import logging
from threading import Thread
from enum import Enum

class ThreadMessageStatus(Enum):
    QUEUED = 1
    PROCESSING = 2
    DONE = 3

class ThreadMessage():
    def __init__(self, msg):
        self.msg = msg
        self.status = ThreadMessageStatus.QUEUED

    def completed(self):
        self.status = ThreadMessageStatus.DONE

    def processing(self):
        self.status = ThreadMessageStatus.PROCESSING

class LocalThread(Thread):
    def __init__(self, thread_message: ThreadMessage, json_upload=True):
        Thread.__init__(self)
        self.thread_message = thread_message
        self.start_time = str(datetime.datetime.now())
        self.json_upload = json_upload

    def completed(self):
        self.thread_message.completed()

    def processing(self):
        self.thread_message.processing()

    def end_time(self):
        return str(datetime.datetime.now())

    def run(self):
        logging.debug(f'Started processing')

        msg = self.thread_message.msg
        print(f"{msg} getting executed")

class LocalThreadPool():
    def __init__(self, json_upload=True):
        self.messages = []
        self.tasks = []
        self.json_upload = json_upload

    def add_tasks(self, messages):
        self.messages = messages
        for msg in self.messages:
            thread_message = ThreadMessage(msg)
            task = LocalThread(thread_message, json_upload=self.json_upload)
            self.tasks.append(task)

    def start_tasks(self):
        for task in self.tasks:
            task.processing()
            task.start()
        return True

    def wait_till_complete(self):
        for task in self.tasks:
            task.join()
            task.completed()


if __name__ == '__main__':
    local_thread_pool_obj = LocalThreadPool()
    local_thread_pool_obj.add_tasks(list(range(100)))
    local_thread_pool_obj.start_tasks()
    local_thread_pool_obj.wait_till_complete()