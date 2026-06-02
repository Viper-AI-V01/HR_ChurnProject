import sys
from src.logger import logging

def error_message_decrypt(error_message,error_detail):
    _,_,sys_error = error_detail.exc_info()
    filename = sys_error.tb_frame.f_code.co_filename
    lineno = sys_error.tb_frame.f_lineno
    
    error__ = 'The error is in [{0}] file in [{1}] LineNo and the error is [{2}] Error'.format(filename,lineno,str(error_message))
    logging.error(error__)
    return error__

class HRmodel_Exception(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_detail)
        self.error_message = error_message_decrypt(error_message,error_detail)
    def __str__(self):
        return self.error_message