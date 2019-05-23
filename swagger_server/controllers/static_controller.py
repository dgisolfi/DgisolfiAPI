import connexion
import six

from swagger_server import util


def add_static(file):  # noqa: E501
    """Upload a static file.

    A static file that will be referenced by the dgisolfi site EX: a picture # noqa: E501

    :param file: Static File
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def get_static(filename):  # noqa: E501
    """Get a static file by name

    Given a static file name in the path, the corresponding file will be returned # noqa: E501

    :param filename: Static Filename
    :type filename: str

    :rtype: None
    """
    return 'do some magic!'
