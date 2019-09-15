
def log_error(log_msg, log_details={}):
    print(log_msg)
    log_details['action'] = 'log_error'


def log_info(log_msg, log_details={}):
    print(log_msg)