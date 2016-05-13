"""
    deviantart.exception
    ^^^^^^^^^^^^^^
    
    Exceptions
    
    :copyright: (c) 2016 by Solimr
"""

class DeviantartError(Exception):

    """Representing API Errors"""

    def __init__(self, httperror, data={}):
        self.message = httperror.__str__()
        if data:
            self.message += "\n{}".format(data["error_description"])
            if "error_details" in data:
                self.message += "\n{}".format("\n".join(data["error_details"]))

    def __str__(self):
        return self.message

class UnauthorizedError(Exception):

    """Representing 401 HTTPError"""

    def __init__(self, httperror, data={}):
        self.message = httperror.__str__()
        if data:
            self.message += "\n{}".format(data["error_description"])
            if "error_details" in data:
                self.message += "\n{}".format("\n".join(data["error_details"]))

    def __str__(self):
        return self.message
