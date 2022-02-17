import logging

class Log():
    # Create and configure logger
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # Creating an object
    logger = logging.getLogger()

    logging.getLogger('').addHandler(console)
    logger = logging.getLogger(__name__)




