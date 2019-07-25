import luigi
import gokart
import pdb

from logtest.task import *

if __name__ == '__main__':
    import logging
    logging.config.fileConfig("./conf/logging.ini")
    print("start tasks")
    logging.info("start tasks")
    gokart.run()
