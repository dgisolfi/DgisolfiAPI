import connexion
import six
import os

from flask import jsonify
from flask import send_file
from swagger_server import util

static_directory = '/usr/src/app/static'


def add_static(file, filename):  # noqa: E501
    """Upload a static file.

    A static file that will be referenced by the dgisolfi site EX: a picture # noqa: E501

    :param file: Static File
    :type file: werkzeug.datastructures.FileStorage
    :param filename: Static Filename
    :type filename: str

    :rtype: None
    """
    try:
        if not os.path.exists(static_directory):
            os.makedirs(static_directory)
        file.save(f'{static_directory}/{filename}')
        file.close()
        return jsonify({'status': 'File Added'}), 201
    except:
        return jsonify({'status': 'File unable to be added'}), 400


def delete_static(filename):  # noqa: E501
    """Delete a static file by name

    Given a static file name in the path, the corresponding file will be deleted # noqa: E501

    :param filename: Static Filename
    :type filename: str

    :rtype: None
    """
    try:
        os.remove(f'{static_directory}/{filename}')
        return jsonify({'status': 'OK'}), 200
    except:
        return jsonify({'status': 'File not found'}), 404


def get_static(filename):  # noqa: E501
    """Get a static file by name

    Given a static file name in the path, the corresponding file will be returned # noqa: E501

    :param filename: Static Filename
    :type filename: str

    :rtype: None
    """
    try:
        return send_file(f'{static_directory}/{filename}'), 200
    except:
        return jsonify({'status': 'File not found'}), 404


def update_static(file, filename):  # noqa: E501
    """Update a Static File.

    Update an existing static file # noqa: E501

    :param file: HTML File
    :type file: werkzeug.datastructures.FileStorage
    :param filename: HTML Filename
    :type filename: str

    :rtype: None
    """
    try:
        os.remove(f'{static_directory}/{filename}')
        file.save(f'{static_directory}/{filename}')
        file.close()
        return jsonify({'status': 'File Updated'}), 201
    except:
        return jsonify({'status': 'File unable to be updated'}), 400
