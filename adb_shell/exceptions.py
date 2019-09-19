"""TODO

"""


from . import constants


class AdbCommandFailureException(Exception):
    """TODO

    """
    def __init__(self, msg):
        super(AdbCommandFailureException, self).__init__(msg)





class DeviceAuthError(Exception):
    """Device authentication failed.

    """
    def __init__(self, message, *args):
        message %= args
        super(DeviceAuthError, self).__init__(message, *args)


class InterleavedDataError(Exception):
    """We only support command sent serially.

    """


class InvalidChecksumError(Exception):
    """Checksum of data didn't match expected checksum.

    """


class InvalidCommandError(Exception):
    """Got an invalid command over USB.

    """
    def __init__(self, message, response_header, response_data):
        if response_header == constants.FAIL:
            message = 'Command failed, device said so. (%s)' % message
        super(InvalidCommandError, self).__init__(message, response_header, response_data)


class InvalidResponseError(Exception):
    """Got an invalid response to our command.

    """


class TcpTimeoutException(Exception):
    """TCP connection timed read/write operation exceeded the allowed time.

    Parameters
    ----------
    msg : str
        TODO

    """
    def __init__(self, msg):
        super(TcpTimeoutException, self).__init__(msg)