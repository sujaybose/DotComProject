import logging


# class LogGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         logging.basicConfig(filename="auto.log", filemode='a',
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger.setLevel(logging.INFO)
#         return logger
#

class LogGen:
        @staticmethod
        def loggen():
            logger = logging.getLogger()
            fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
            return logger


#
# logger= LogGen.loggen()
# logger.info("****Started Home Page Title Test ****")