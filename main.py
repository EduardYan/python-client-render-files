"""
This is a small program
for make a client from a server of files.

"""

# from simplejson.errors import JSONDecodeError
from models.client import Client
from optparse import OptionParser
from messages.initials import INITIAL_MESSAGE
from models.error import Error
from helpers.utils import ask_save_output, show_content_request
from doc.commands_doc import HELP_MESSAGE

def get_options():
  """
  Return a the options of the methods GET, POST, PUT, DELETE
  for make the client and make the request to server.
  """

  parser = OptionParser()
  parser.add_option('-m', '--method', dest = 'method', help = HELP_MESSAGE)
  parser.add_option('-f', '--file', dest = 'file_server', help = 'Put the file with the direction of the server for make the request.')

  options, args = parser.parse_args()

  if not options.method:
    parser.error('Put a method for make the request. Fore see more information execute --help flag.')

  if not options.file_server:
    parser.error('Put the file with the direction of the server for make the request.')

  return options


def main() -> None:
  """
  This is the principal function for execute
  the client.
  """
  # gettings the values of the options
  options = get_options()
  method = options.method
  file_server = options.file_server # getting the file of the config server

  print(INITIAL_MESSAGE) # showing initial message

  # validating the methods and controlling the exceptions
  if method == 'get' or method == 'GET':
    try:
      clientFiles = Client(file_server)
      output = clientFiles.make_request_get()

      if ask_save_output():
        path_file = input('Path from file for save the output > ')
        clientFiles.save_request_get(output, path_file)

      else:
        show_content_request('get', output)

    except FileNotFoundError:
      error = Error('[-] The file of the server not found in the system.')
      print(error)

    except IsADirectoryError: # in case the path is a directory
      error = Error('[-] The path for save the file is a directory !!')
      print(error)

    except OSError:
      error = Error('[-] Some problem with the network of the system.')
      print(error)

    except ConnectionError:  # in case bad connection
      error = Error('[-] Some problem with the connection with the server, try restart the server.')
      print(error)

  if method == 'get-file' or method == 'GET-FILE':
    try:
      id_file = input('Id File > ')
      clientFiles = Client(file_server)
      output = clientFiles.make_request_get_file(id_file)

      if ask_save_output(): # validating if save the file
        path_file = input('Path from file for save the output > ')
        clientFiles.save_request_get_file(output['content'], path_file)

      else: show_content_request('get-file', output)

    except KeyError: # in case the id of the file not found
      error = Error('\n[-] Id of the file not found. In the server.')
      print(error)

    except FileNotFoundError: # in case the file of the server not found
      error = Error('\n[-] The file from the direction for the server. Not found.')
      print(error)

    except IsADirectoryError: # in case be a directory
      error = Error('\n[-] The path for save the file is a directory !!')
      print(error)

    except OSError: # this is in case some error with the operative system
      error = Error('\n[-] Some problem with the network of the system. Try again. Or verify the direction of the server in the file.')
      print(error)

    except ConnectionError:  # in case bad connection
      error = Error('\n[-] Some problem with the connection with the server, try restart the server.')
      print(error)


  if method == 'post' or method == 'POST':
    try:
      print('\nPut the data for send at server.')
      data = input('Data (Sample /home/user/hello.txt ) > ')
      clientFiles = Client(file_server)
      output = clientFiles.make_request_post(data)

      if ask_save_output():
        path_file = input('Path from file for save the output > ')
        clientFiles.save_request_post(output, path_file)

      else:
        show_content_request('post', output)

    except IsADirectoryError: # in case be a directory
      error = Error('\n[-] The path for save the file is a directory !!')
      print(error)
 
    except OSError:
      error = Error('\n[-] Some problem with the network of the system.')
      print(error)

    except ConnectionError:  # in case bad connection
      error = Error('\n[-] Some problem with the connection with the server, try restart the server.')
      print(error)

  if method == 'put' or method == 'PUT':
    try:
      clientFiles = Client(file_server)
      o = clientFiles.make_request_put()
      print(o)

    except OSError:
      error = Error('Some problem with the network of the system.')
      print(error)

    except ConnectionError:  # in case bad connection
      error = Error('Some problem with the connection with the server, try restart the server.')
      print(error)

  if method == 'delete' or method == 'DELETE':
    try:
      clientFiles = Client(file_server)
      o = clientFiles.make_request_delete()
      print(o)

    except OSError:
      error = Error('Some problem with the network of the system.')
      print(error)

    except ConnectionError:  # in case bad connection
      error = Error('Some problem with the connection with the server, try restart the server.')
      print(error)


if __name__ == '__main__':
  main()