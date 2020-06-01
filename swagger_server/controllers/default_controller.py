import connexion
import six

from swagger_server import util
from CouchClient.couch import CouchClient


def pages_get(page):  # noqa: E501
    """Returns the content of a page

     # noqa: E501

    :param page: 
    :type page: str

    :rtype: List[str]
    """
    client = CouchClient()
    return client._find(
        {
            "selector": {
                "page": {
                    "$eq": page
                }
            }
        }
    )
