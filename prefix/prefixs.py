"""
This module have the prefix to put
when to make the requests.
"""

# some prefix for concat with each route of the server
PREFIX_POST = '/add-path/'
PREFIX_PUT = '/update-path/{id}' # these route recived the id for pass
PREFIX_DELETE = '/delete-path/{id}'
PREFIX_GET_FILE = '/get-file/{id}'