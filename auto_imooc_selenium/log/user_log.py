import datetime
import logging
import os.path


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.Logger.manager.loggerDict.pop(__name__)
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

        # file name
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = "{}/{}".format(log_dir, log_file)

        # file output logs
        self.file_handlers = logging.FileHandler(log_name, "a", encoding="utf-8")
        self.file_handlers.setLevel(logging.INFO)
        file_format = logging.Formatter(
            "%(asctime)s %(filename)s-> %(funcName)s %(levelno)s: %(levelname)s -->%(message)s")
        self.file_handlers.setFormatter(file_format)
        self.logger.addHandler(self.file_handlers)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handlers)
        self.file_handlers.close()


"""if __name__ == '__main__':
    ul = UserLog()
    log = ul.get_log()
    log.info("hie")
    ul.close_handle()"""
