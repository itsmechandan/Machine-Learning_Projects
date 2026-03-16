import sys 
# error_detail: sys is a type hint (type annotation).
# It tells readers and tools what type of object error_detail is expected to be.
def error_message_detail(error,error_detail:sys):
    # the 3rd argument of exc_info gives the file name, location 
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in script name [{0}], Line Number [{1}], error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
         
    )
    return error_message

class CustomeException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail = error_detail)

    def __str__(self):
        return self.error_message


    


    