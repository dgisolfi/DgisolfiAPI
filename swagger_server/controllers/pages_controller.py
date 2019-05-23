import connexion
import six

from swagger_server import util


def add_page(file):  # noqa: E501
    """Upload a HTML Page.

    A HTML file that will be referenced by the dgisolfi website # noqa: E501

    :param file: HTML File
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def get_page(filename):  # noqa: E501
    """Get a html file by page name

    Given a page name in the path, the corresponding html file will be returned # noqa: E501

    :param filename: HTML Filename
    :type filename: str

    :rtype: None
    """
    return 'do some magic!'


def update_page(file):  # noqa: E501
    """Update a HTML Page.

    Update an existing HTML file # noqa: E501

    :param file: HTML File
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'
