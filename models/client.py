"""
This module have the class Client
for create a client.
"""

from requests import get, post, put, delete
from data.paths import DEFAULT_PATH_TO_SAVE
from prefix.prefixs import PREFIX_POST, PREFIX_DELETE, PREFIX_PUT, PREFIX_GET_FILE
from json import dumps, JSONDecodeError

class Client:
  """
  Create a Client object
  with a name and methods for make request
  of the server.
  
  For default alls the methods for save the output
  in a file using the DEFAULT_PATH_TO_SAVE:

  /home/user_current/Downloads/

  """

  def __init__(self, file_server) -> None:
    # initials values for the client
    self.file_server = file_server

  def get_file_request(self):
    """
    Return the first line in string, of the file
    server.txt, with the direction of the server for make
    the request.
    """

    with open(self.file_server, 'r') as f:
      lines = f.readlines()

    return lines[0].strip('\n')


  def make_request_get(self) -> dict:
    """
    Make the request in case be a get.
    """

    direction = self.get_file_request()

    request = get(direction)
    content = request.json()

    return content


  def make_request_get_file(self, id:str = 0) -> dict:
    """
    Make the request for get a file.
    """

    if type(id) not in [str]:
      raise TypeError('The id must be a string.')

    direction = self.get_file_request()

    try:
      request = get(direction + PREFIX_GET_FILE.format(id = id))
      content = request.json()

      return content

    # hacemos esta excepcion para que si el id, del archivo como valor tenga letras o numeros
    # porque si no nos lanzara la exepcion de JSONDecodeError
    except JSONDecodeError:
      raise KeyError('Id of the file not found. In the server.')


  def make_request_post(self, data:str) -> dict:
    """
    Make the request in case be a post.
    Send the data passed for parameter.
    """

    if type(data) not in [str]:
      raise TypeError('The data must be a string.')

    direction = self.get_file_request()

    try:
      # getting the request and sending the data as path=data
      request = post(direction + PREFIX_POST, {'path': data})
      content = request.json()

      return content

    except:
      print('Some error')

  def make_request_put(self, id:str, data:str) -> dict:
    """
    Make the request in case be a put.
    Update the data passed for parameter.
    """

    if type(id) not in [str]:
      raise TypeError('The id must be a string.')
    if type(data) not in [str]:
      raise TypeError('The data must be a string.')

    direction = self.get_file_request()

    try:
      request = put(direction + PREFIX_PUT.format(id = id), {'path': data})
      content = request.json()

      return content

    except JSONDecodeError:
      raise KeyError('Id of the file not found. In the server.')


  def make_request_delete(self, id:str = 0) -> dict:
    """
    Make the request in case be a delete.
    The id passed for parameter, try send the request.

    The id for default is 0.
    """

    if type(id) not in [str]:
      raise TypeError('The id must be a string.')

    direction = self.get_file_request()

    try:
      request = delete(direction + PREFIX_DELETE.format(id = id))
      content = request.json()

      return content

    except JSONDecodeError:
      raise KeyError('Id of the file not found. In the server.')

  def save_request_get(self, content:str, file_to_save = DEFAULT_PATH_TO_SAVE):
    """
    Save the content of the request get passed for parameter.
    """

    with open(file_to_save, 'w') as f:
      content = dumps(content, indent = 4) # saving the file with json format
      f.write(str(content))

    print( f'\n[+] Succesfully saved for get request in {file_to_save}' )

  def save_request_get_file(self, content:str, file_to_save = DEFAULT_PATH_TO_SAVE):
    """
    Save the content of the request passed for parameter.
    """

    with open(file_to_save, 'w') as f: # wrinting in the file
      for line in content:
        f.write(str(line))

    print( f'\n[+] Succesfully saved for get-file request in {file_to_save}' )

  def save_request_post(self, content:str, file_to_save = DEFAULT_PATH_TO_SAVE):
    """
    Save the content of the request post passed for parameter.
    """

    # open the file for writing
    with open(file_to_save, 'w') as f: # wrinting in the file
        content = dumps(content, indent = 4) # formating the content for save
        f.write(str(content))

    print( f'\n[+] Succesfully saved for post request in {file_to_save}' )

  def save_request_put(self, content:str, file_to_save = DEFAULT_PATH_TO_SAVE):
    """
    Save the content of the request put passed for parameter.
    """

    # open the file for writing
    with open(file_to_save, 'w') as f: # wrinting in the file
        content = dumps(content, indent = 4)
        f.write(content)

    print( f'\n[+] Succesfully saved for put request in {file_to_save}' )

  def save_request_delete(self, content:str, file_to_save = DEFAULT_PATH_TO_SAVE):
    """
    Save the content of the request delete passed for parameter.
    """

    # open the file for writing
    with open(file_to_save, 'w') as f: # wrinting in the file
        content = dumps(content, indent = 4)
        f.write(str(content))

    print( f'\n[+] Succesfully saved for put request in {file_to_save}' )


  def __str__(self) -> str:
      return f'This is a client {self.nameClient}'