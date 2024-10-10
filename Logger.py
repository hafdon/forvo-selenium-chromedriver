import logging


class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()
        return Logger._instance

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton")
        else:
            logging.basicConfig(
                filename="found_words.log",
                filemode="a",  # append
                format="%(asctime)s - %(levelname)s - %(message)s",
                level=logging.info,
            )
            Logger._instance = self

    @staticmethod
    def log_message(message):
        print(message)
        logging.info(message)
