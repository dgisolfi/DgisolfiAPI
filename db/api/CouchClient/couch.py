#!/usr/bin/python3

import os
import pycouchdb
import requests
import json


class CouchClient:
    """
    CouchDB Client

    A merge of the limited, but useful pycouchdb along with some 
    additional features that can be leveraged through CouchDB's API.

    There are no public Attributes for this class
    """

    def __init__(self):
        # Database Information
        self._user = os.getenv("COUCHDB_USER", None)
        self._password = os.getenv("COUCHDB_PASSWORD", None)
        self._host = os.getenv("COUCHDB_HOST", None)
        self._port = os.getenv("COUCHDB_PORT", 5984)
        self._db_name = os.getenv("COUCHDB_DB", None)
        self._conn_url = (
            f"http://{self._user}:{self._password}@{self._host}:{self._port}"
        )

        # create a connection
        self._couch = self._connect()
        # Get or create the db
        self._db = self._getDatabase()

    def _connect(self):
        """
        Get a new connection object to the database

        Raises
        ------
        Cannot Connect to CouchDB
            If the connection to the conn_url fails 
            this will be raised

        Returns
        -------
        connection : pycouchdb object
            client for couchdb
        """
        try:
            return pycouchdb.Server(self._conn_url)
        except:
            raise ValueError("Cannot Connect to CouchDB")

    def _getDatabase(self):
        """
        Gets or Creates a database within couchdb

        Returns
        -------
        db : pycouchdb database connection
            a database connection for the specifed db_name
        """
        if self._db_name in self._couch:
            return self._couch.database(self._db_name)
        else:
            return self._couch.create(self._db_name)

    """ Basic interactions from pycouchdb """

    def _get(self, _id):
        """ gets a couchdb document by _id """
        return self._db.get(_id)

    def _create(self, obj):
        """ creates a new document with the contents of obj """
        return self._db.save(obj)

    def _delete(self, _id):
        """ removes a document specified by _id """
        return self._db.delete(_id)

    """ Additional Methods """

    def _find(self, query):
        """
        Runs a mango query on the couchdb instance

        Parameters
        ----------
        query : dictionary
            a mango query for couchdb...if you dont know it look it up
        Raises
        ------
        Error while running find on given selector
            find error from database
        Returns
        -------
        docs : array
            all docs that meet the specified query
        """
        response = requests.post(f"{self._conn_url}/{self._db_name}/_find", json=query)
        if response.status_code is not 200:
            raise ValueError("Error while running find on given selector")
        else:
            return response.json()["docs"]

    def _update(self, _id, json):
        """
        Updates an existing document by setting the value to that 
        of the given param

        Parameters
        ----------
        _id : string
            the unique document ID of the doc to be updated
        json : dictionary
            the value the doc should be updated to
        Raises
        ------
        Error while updating document
            update error from database
        Returns
        -------
        doc : dictionary
            the updated version of the document, or the details on why 
            it was not updated
        """
        doc = self._get(_id)
        json["_rev"] = doc["_rev"]

        response = requests.put(f"{self._conn_url}/{self._db_name}/{_id}", json=json)
        if response.status_code is not 201:
            raise ValueError("Error while updating document")
        else:
            return response.json()
            