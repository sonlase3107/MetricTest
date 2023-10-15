import logging


def logging_ins(pathfile:str):
    logsys = logging
    logsys.basicConfig(filename=pathfile,level=logging.INFO, filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    return logsys